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

# docx media number -> output slug. 2/4 are the dark-background wordmarks (EN/IS) shown in
# the footer; 3 (light Icelandic wordmark) is the source of the header horse mark + favicon.
FOOTER_MARKS = {4: "logo-footer-is", 2: "logo-footer-en"}
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

# Pixel-rotated sources with no EXIF orientation tag, keyed by docx media number
# (degrees counterclockwise to apply).
ROTATE = {
    19: -90,  # svartstjarna
    28: 90,  # gallery 09: lighthouse
    29: -90,  # gallery 10: rider with two horses
    42: 90,  # gallery 23: white horse, timestamped
    59: -90,  # gallery 40: Arnar with chestnut and black horse
    61: -90,  # gallery 42: horses above waterfall
}

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


def save_footer_mark(img: Image.Image, dest: Path) -> None:
    """Dark-background wordmark -> white line art on transparency for the footer."""
    gray = img.convert("L")
    # The source JPEGs carry a thin light frame at the very edge; cut it before trimming.
    inset = max(3, gray.width // 40)
    gray = gray.crop((inset, inset, gray.width - inset, gray.height - inset))
    bbox = gray.point(lambda v: 255 if v > 40 else 0).getbbox()
    if bbox is None:
        raise ValueError("footer wordmark contains no line art")
    gray = gray.crop(bbox)
    target_h = 220  # rendered at ~110px -> 2x for high-dpi screens
    gray = gray.resize(
        (int(gray.width * target_h / gray.height), target_h), Image.Resampling.LANCZOS
    )
    rgba = Image.new("RGBA", gray.size, (255, 255, 255, 0))
    rgba.putalpha(gray)  # brightness becomes opacity: black bg vanishes, white lines stay
    dest.parent.mkdir(parents=True, exist_ok=True)
    rgba.save(dest, "WEBP", lossless=True, method=6)


def horse_art(img: Image.Image, target_h: int) -> Image.Image:
    """Extract the horse line art from the light wordmark logo, as grayscale.

    The source is thin light line art over the top ~2/3, with the wordmark text below.
    Crop the art, trim the margins, then thicken the strokes (MinFilter dilates dark
    pixels) so they survive small display sizes.
    """
    from PIL import ImageFilter

    gray = img.convert("L")
    art = gray.crop((0, 0, gray.width, int(gray.height * 0.68)))
    bbox = art.point(lambda v: 255 if v < 230 else 0).getbbox()
    if bbox is None:
        raise ValueError("logo crop contains no line art")
    art = art.crop(bbox).filter(ImageFilter.MinFilter(3))
    return art.resize((int(art.width * target_h / art.height), target_h), Image.Resampling.LANCZOS)


def save_logo_mark(img: Image.Image, dest: Path) -> None:
    """Horse line art on transparency, for the site header (the wordmark text is HTML)."""
    art = horse_art(img, target_h=192)  # rendered at 48px -> 4x for high-dpi screens
    rgba = Image.new("RGBA", art.size, (40, 40, 40, 0))
    rgba.putalpha(art.point(lambda v: 255 - v))  # white -> transparent
    dest.parent.mkdir(parents=True, exist_ok=True)
    rgba.save(dest, "WEBP", lossless=True, method=6)


def save_favicon(img: Image.Image, dest: Path) -> None:
    """Horse line art centered on a white square, visible in any browser tab theme."""
    art = horse_art(img, target_h=128).convert("RGB")  # oversample, then fit
    art.thumbnail((56, 56), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (64, 64), "white")
    canvas.paste(art, ((64 - art.width) // 2, (64 - art.height) // 2))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest, "PNG")


def save_og_image(cover: Path, dest: Path) -> None:
    """1200x630 JPEG social-preview crop of the hero photo (JPEG for scraper support)."""
    img = Image.open(cover).convert("RGB")
    img = ImageOps.fit(img, (1200, 630), Image.Resampling.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "JPEG", quality=85, optimize=True)


def main() -> None:
    docx = next(ROOT.glob("*íslenska*.docx"))
    print(f"Reading media from {docx.name}")
    media = load_media(docx)

    for num, slug in FOOTER_MARKS.items():
        save_footer_mark(open_image(media[num]), IMAGES / f"{slug}.webp")
        print(f"  logo    image{num} -> {slug}.webp")

    save_logo_mark(open_image(media[3]), IMAGES / "logo-mark.webp")
    print("  logo    image3 -> logo-mark.webp (horse art only)")

    save_favicon(open_image(media[3]), IMAGES / "favicon.png")
    print("  logo    image3 -> favicon.png")

    save_og_image(IMAGES / "cover.webp", IMAGES / "og-image.jpg")
    print("  social  cover.webp -> og-image.jpg (1200x630)")

    for num, slug in PORTRAITS.items():
        img = open_image(media[num])
        if num in ROTATE:
            img = img.rotate(ROTATE[num], expand=True)
        save_photo(img, IMAGES / f"{slug}.webp", PORTRAIT_MAX, 82)
        print(f"  portrait image{num} -> {slug}.webp")

    for idx, num in enumerate(GALLERY_RANGE, start=1):
        src = open_image(media[num])
        if num in ROTATE:
            src = src.rotate(ROTATE[num], expand=True)
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
