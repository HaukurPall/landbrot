"""One-off image pipeline for landbrot.is.

Extracts the photos embedded in the Icelandic source .docx (the German file holds
byte-identical media), then resizes and converts everything to optimized WebP under
``images/``. Run this whenever Arnar sends new photos:

    uv run optimize_images.py

The committed WebP files are what the site ships; ``build.py`` only copies them, so the
deploy pipeline needs no image tooling.
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).parent
IMAGES = ROOT / "images"
GALLERY = IMAGES / "gallery"

# docx media number -> output slug for logos and horse portraits.
LOGOS = {
    1: "logo-en",
    3: "logo-is",
}  # 1 = English wordmark, 3 = Icelandic wordmark (light bg)
PORTRAITS = {
    6: "lyfting",
    7: "freyja",
    8: "thokkadis",
    9: "dogun",
    10: "gna",
    11: "katla",
    12: "hekla",
    13: "gersemi",
    14: "kjarkur",
    15: "blesi",
    16: "baldur",
    17: "blaer",
    18: "askur",
    19: "svartstjarna",
}
GALLERY_RANGE = range(20, 66)  # image20..image65 -> 46 gallery photos

PORTRAIT_MAX = 1100
GALLERY_MAX = 1600
THUMB_MAX = 640


def load_media(docx: Path) -> dict[int, bytes]:
    """Return {image number: raw bytes} for every word/media/imageN.* in the docx."""
    media = {}
    with zipfile.ZipFile(docx) as zf:
        for name in zf.namelist():
            stem = Path(name).stem  # imageN
            if name.startswith("word/media/image") and stem[5:].isdigit():
                media[int(stem[5:])] = zf.read(name)
    return media


def open_image(raw: bytes) -> Image.Image:
    img = Image.open(io.BytesIO(raw))
    img.load()
    return ImageOps.exif_transpose(img)


def save_photo(img: Image.Image, dest: Path, max_side: int, quality: int) -> None:
    img = img.convert("RGB")
    img.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "WEBP", quality=quality, method=6)


def save_logo(img: Image.Image, dest: Path) -> None:
    # Line art with text: keep it crisp with lossless WebP.
    img = img.convert("RGBA")
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "WEBP", lossless=True, method=6)


def main() -> None:
    docx = next(ROOT.glob("*íslenska*.docx"))
    print(f"Reading media from {docx.name}")
    media = load_media(docx)

    for num, slug in LOGOS.items():
        save_logo(open_image(media[num]), IMAGES / f"{slug}.webp")
        print(f"  logo    image{num} -> {slug}.webp")

    for num, slug in PORTRAITS.items():
        save_photo(open_image(media[num]), IMAGES / f"{slug}.webp", PORTRAIT_MAX, 82)
        print(f"  portrait image{num} -> {slug}.webp")

    for idx, num in enumerate(GALLERY_RANGE, start=1):
        src = open_image(media[num])
        save_photo(src.copy(), GALLERY / f"{idx:02d}.webp", GALLERY_MAX, 80)
        save_photo(src.copy(), GALLERY / f"{idx:02d}_thumb.webp", THUMB_MAX, 72)
    print(
        f"  gallery image{GALLERY_RANGE.start}..{GALLERY_RANGE.stop - 1} -> gallery/01..{len(GALLERY_RANGE):02d}"
    )

    # Hero cover comes from the existing repo asset, not the docx.
    cover = IMAGES / "cover.jpg"
    if cover.exists():
        save_photo(open_image(cover.read_bytes()), IMAGES / "cover.webp", 1920, 80)
        print("  cover   cover.jpg -> cover.webp")


if __name__ == "__main__":
    main()
