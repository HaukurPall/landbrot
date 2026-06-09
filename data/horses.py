"""Language-neutral horse data for landbrot.is.

One entry per horse in :data:`HORSES`; the templates render each in both Icelandic and
German. Strings that genuinely differ between languages (event/class/round names) are stored
as ``{"is": ..., "de": ...}`` dicts built with :func:`bl`; horse and farm names are the same
in both languages and only the connective (frá / von) is localized at render time.

FEIF/WorldFengur registration numbers are transcribed from the source documents using the
offspring tables as the authoritative source where a horse's number appeared inconsistently
(see README / build notes for the handful of corrections confirmed with the owner).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


def bl(is_: str, de: str | None = None, en: str | None = None) -> dict[str, str]:
    """Localized string; ``de``/``en`` default to the Icelandic value when identical
    (proper nouns like event names stay Icelandic in every language)."""
    return {"is": is_, "de": de if de is not None else is_, "en": en if en is not None else is_}


class Sex(StrEnum):
    MARE = "mare"
    STALLION = "stallion"
    GELDING = "gelding"


class Category(StrEnum):
    FOUNDATION = "foundation"  # ættmóðir — featured on the home page only
    BREEDING_MARE = "breeding_mare"  # ræktunarhryssur / Zuchtstuten
    YOUNG_MARE = "young_mare"  # unghryssur / junge Stuten
    YOUNG_MALE = "young_male"  # unghestar / junge Hengste
    RIDING_HORSE = "riding_horse"  # reiðhross / Reitpferde


@dataclass(frozen=True)
class Ref:
    """A horse referenced by name, e.g. a sire, dam or offspring."""

    name: str
    farm: str
    feif_id: str | None = None


@dataclass(frozen=True)
class Score:
    total: float  # aðaleinkunn / Gesamtnote
    conformation: float  # bygging / Exterieur
    rideability: float  # hæfileikar / Reiteigenschaften


@dataclass(frozen=True)
class Assessment:
    """Breeding assessment (kynbótadómur). age/year are absent for foundation mares."""

    score: Score
    age: int | None = None
    year: int | None = None


@dataclass(frozen=True)
class CompRow:
    rider: str
    discipline: dict[str, str]
    klass: dict[str, str]
    phase: dict[str, str]
    score: float
    rank: str | None = None


@dataclass(frozen=True)
class CompEvent:
    date: str
    event_id: str
    name: dict[str, str]
    rows: tuple[CompRow, ...]


@dataclass(frozen=True)
class Offspring:
    ref: Ref
    sire: Ref
    sex: Sex
    score: Score | None = None


@dataclass(frozen=True)
class Horse:
    ref: Ref
    category: Category
    sire: Ref
    dam: Ref
    sex: Sex
    image: str | None = None
    featured: bool = False  # also shown on the home page
    assessment: Assessment | None = None
    results: tuple[CompEvent, ...] = ()
    offspring: tuple[Offspring, ...] = ()


def tb(name: str, feif: str | None = None) -> Ref:
    """Reference to a horse bred at Þykkvabæ I."""
    return Ref(name, "Þykkvabæ I", feif)


# --- Foundation / breeding mares -------------------------------------------------------

LYFTING = Horse(
    ref=tb("Lyfting", "IS2006285260"),
    category=Category.BREEDING_MARE,
    sex=Sex.MARE,
    sire=Ref("Þokki", "Kýrholti", "IS1997158430"),
    dam=tb("Jörp", "IS1996285260"),
    image="lyfting",
    featured=True,
    assessment=Assessment(Score(total=8.08, conformation=7.72, rideability=8.32), age=5, year=2011),
    results=(
        CompEvent(
            date="18.07.2018",
            event_id="IS2018SPR153",
            name=bl(
                "Íslandsmót í hestaíþróttum",
                "Isländische Reitmeisterschaften",
                "Icelandic Equestrian Championships",
            ),
            rows=(
                CompRow(
                    "Helga Una Björnsdóttir",
                    bl("Tölt T2"),
                    bl("Master class", "Meisterklasse"),
                    bl("Forkeppni", "Vorentscheidung", "Preliminary round"),
                    7.67,
                    "3.",
                ),
                CompRow(
                    "Helga Una Björnsdóttir",
                    bl("Tölt T2"),
                    bl("Master class", "Meisterklasse"),
                    bl("A úrslit", "A-Finale", "A-final"),
                    7.38,
                    "3.",
                ),
            ),
        ),
        CompEvent(
            date="26.07.2012",
            event_id="IS2012GEY103",
            name=bl(
                "Íslandsmót barna-, unglinga- og ungmennaflokka",
                "Isländische Jugendmeisterschaften",
                "Icelandic Youth Championships",
            ),
            rows=(
                CompRow(
                    "Oddur Ólafsson",
                    bl("Tölt T2"),
                    bl("Ungmennaflokkur", "Jugendklasse", "Young adults class"),
                    bl("A úrslit", "A-Finale", "A-final"),
                    7.08,
                    "1.",
                ),
                CompRow(
                    "Oddur Ólafsson",
                    bl("Fimmgangur F1", "Fünfgang F1", "Five gait F1"),
                    bl("Ungmennaflokkur", "Jugendklasse", "Young adults class"),
                    bl("B úrslit", "B-Finale", "B-final"),
                    6.00,
                    "5.",
                ),
            ),
        ),
        CompEvent(
            date="25.06.2012",
            event_id="IS2012LM0057",
            name=bl("Landsmót hestamanna 2012"),
            rows=(
                CompRow(
                    "Oddur Ólafsson",
                    bl(""),
                    bl("Ungmennaflokkur", "Jugendklasse", "Young adults class"),
                    bl("Undanúrslit", "Semifinale", "Semi-finals"),
                    8.32,
                    "25.",
                ),
            ),
        ),
        CompEvent(
            date="31.05.2012",
            event_id="IS2012SLE062",
            name=bl("Opið Gæðingamót Sleipnis, Ljúfs og Háfeta"),
            rows=(
                CompRow(
                    "Oddur Ólafsson",
                    bl(""),
                    bl("Ungmennaflokkur", "Jugendklasse", "Young adults class"),
                    bl("A úrslit", "A-Finale", "A-final"),
                    8.42,
                    "2.",
                ),
            ),
        ),
    ),
    offspring=(
        Offspring(
            tb("Blesi", "IS2013185260"), Ref("Konsert", "Korpu", "IS2005101001"), Sex.GELDING
        ),
        Offspring(
            tb("Blakkur", "IS2014185260"),
            tb("Hrannar frá Flugumýri II", "IS2006158620"),
            Sex.STALLION,
            Score(total=8.41, conformation=8.51, rideability=8.35),
        ),
        Offspring(
            tb("Baldur", "IS2015185260"), Ref("Arður", "Brautarholti", "IS2001137637"), Sex.GELDING
        ),
        Offspring(
            tb("Gná", "IS2016285260"),
            tb("Hrannar frá Flugumýri II", "IS2006158620"),
            Sex.MARE,
            Score(total=8.46, conformation=8.27, rideability=8.55),
        ),
        Offspring(tb("Blær", "IS2019185260"), Ref("Konsert", "Hofi", "IS2010156107"), Sex.GELDING),
        Offspring(
            tb("Gjósta", "IS2020285260"), tb("Hrannar frá Flugumýri II", "IS2006158620"), Sex.MARE
        ),
        Offspring(
            tb("Gersemi", "IS2023285260"), Ref("Skarpur", "Kýrholti", "IS2015158431"), Sex.MARE
        ),
        Offspring(
            tb("Gleði", "IS2024285260"), tb("Hrannar frá Flugumýri II", "IS2006158620"), Sex.MARE
        ),
        Offspring(
            tb("Gefjun", "IS2025285260"), Ref("Fróði", "Flugumýri", "IS2017158627"), Sex.MARE
        ),
    ),
)

FREYJA = Horse(
    ref=Ref("Freyja", "Prestsbakka", "IS1993285026"),
    category=Category.FOUNDATION,
    sex=Sex.MARE,
    sire=Ref("Gnýr", "Hrepphólum", "IS1988188170"),
    dam=Ref("Gyðja", "Gerðum", "IS1982286002"),
    image="freyja",
    featured=True,
    assessment=Assessment(Score(total=8.03, conformation=8.08, rideability=7.99)),
)

THOKKADIS = Horse(
    ref=tb("Þokkadís", "IS2008285260"),
    category=Category.BREEDING_MARE,
    sex=Sex.MARE,
    sire=Ref("Þokki", "Kýrholti", "IS1997158430"),
    dam=Ref("Freyja", "Prestsbakka", "IS1993285026"),
    image="thokkadis",
    assessment=Assessment(Score(total=7.99, conformation=7.68, rideability=8.20), age=4, year=2012),
    offspring=(
        Offspring(
            tb("Askur", "IS2018185260"), Ref("Apollo", "Haukholtum", "IS2012188158"), Sex.GELDING
        ),
    ),
)

DOGUN = Horse(
    ref=tb("Dögun", "IS2009285260"),
    category=Category.BREEDING_MARE,
    sex=Sex.MARE,
    sire=Ref("Ómur", "Kvistum", "IS2003181962"),
    dam=Ref("Freyja", "Prestsbakka", "IS1993285026"),
    image="dogun",
    assessment=Assessment(Score(total=8.39, conformation=8.35, rideability=8.42), age=7, year=2016),
    offspring=(
        Offspring(tb("Katla", "IS2020285261"), tb("Baldur", "IS2015185260"), Sex.MARE),
        Offspring(
            tb("Eldgjá", "IS2021285260"),
            Ref("Jökull", "Breiðholti í Flóa", "IS2013182591"),
            Sex.MARE,
        ),
        Offspring(tb("Hekla", "IS2022285260"), tb("Blakkur", "IS2014185260"), Sex.MARE),
        Offspring(
            tb("Laki", "IS2023185260"), Ref("Skarpur", "Kýrholti", "IS2015158431"), Sex.GELDING
        ),
        Offspring(
            tb("Nn", "IS2024185261"), tb("Hrannar frá Flugumýri II", "IS2006158620"), Sex.STALLION
        ),
        Offspring(tb("Nm", "IS2025185261"), Ref("Lexus", "Vatnsleysu"), Sex.STALLION),
    ),
)

GNA = Horse(
    ref=tb("Gná", "IS2016285260"),
    category=Category.BREEDING_MARE,
    sex=Sex.MARE,
    sire=tb("Hrannar frá Flugumýri II", "IS2006158620"),
    dam=tb("Lyfting", "IS2006285260"),
    image="gna",
    assessment=Assessment(Score(total=8.46, conformation=8.27, rideability=8.55), age=7, year=2023),
    results=(
        CompEvent(
            date="19.08.2022",
            event_id="IS2022GEY211",
            name=bl("WR Suðurlandsmót"),
            rows=(
                CompRow(
                    "Helga Una Björnsdóttir",
                    bl("Fimmgangur F2", "Fünfgang F2", "Five gait F2"),
                    bl("Meistaraflokkur", "Meisterklasse", "Master class"),
                    bl("Forkeppni", "Vorentscheidung", "Preliminary round"),
                    7.03,
                    "2.",
                ),
            ),
        ),
    ),
    offspring=(
        Offspring(tb("Nn", "IS2024185260"), Ref("Þráinn", "Flagbjarnarholti"), Sex.STALLION),
        Offspring(
            tb("Óðinn", "IS2025185260"), Ref("Skýr", "Skálakoti", "IS2007184162"), Sex.STALLION
        ),
    ),
)

# --- Young horses ----------------------------------------------------------------------

YOUNG = (
    Horse(
        tb("Katla", "IS2020285261"),
        Category.YOUNG_MARE,
        tb("Baldur", "IS2015185260"),
        tb("Dögun", "IS2009285260"),
        Sex.MARE,
        image="katla",
    ),
    Horse(
        tb("Eldgjá", "IS2021285260"),
        Category.YOUNG_MARE,
        Ref("Jökull", "Breiðholti í Flóa", "IS2013182591"),
        tb("Dögun", "IS2009285260"),
        Sex.MARE,
    ),
    Horse(
        tb("Hekla", "IS2022285260"),
        Category.YOUNG_MARE,
        tb("Blakkur", "IS2014185260"),
        tb("Dögun", "IS2009285260"),
        Sex.MARE,
        image="hekla",
    ),
    Horse(
        tb("Gjósta", "IS2020285260"),
        Category.YOUNG_MARE,
        tb("Hrannar frá Flugumýri II", "IS2006158620"),
        tb("Lyfting", "IS2006285260"),
        Sex.MARE,
    ),
    Horse(
        tb("Gersemi", "IS2023285260"),
        Category.YOUNG_MARE,
        Ref("Skarpur", "Kýrholti", "IS2015158431"),
        tb("Lyfting", "IS2006285260"),
        Sex.MARE,
        image="gersemi",
    ),
    Horse(
        tb("Gleði", "IS2024285260"),
        Category.YOUNG_MARE,
        tb("Hrannar frá Flugumýri II", "IS2006158620"),
        tb("Lyfting", "IS2006285260"),
        Sex.MARE,
    ),
    Horse(
        tb("Gefjun", "IS2025285260"),
        Category.YOUNG_MARE,
        Ref("Fróði", "Flugumýri", "IS2017158627"),
        tb("Lyfting", "IS2006285260"),
        Sex.MARE,
    ),
    Horse(
        tb("Laki", "IS2023185260"),
        Category.YOUNG_MALE,
        Ref("Skarpur", "Kýrholti", "IS2015158431"),
        tb("Dögun", "IS2009285260"),
        Sex.GELDING,
    ),
    Horse(
        tb("Óðinn", "IS2025185260"),
        Category.YOUNG_MALE,
        Ref("Skýr", "Skálakoti", "IS2007184162"),
        tb("Gná", "IS2016285260"),
        Sex.STALLION,
    ),
)

# --- Riding horses ---------------------------------------------------------------------

RIDING = (
    Horse(
        Ref("Kjarkur", "Prestsbakka", "IS2002185028"),
        Category.RIDING_HORSE,
        Ref("Magni", "Prestsbakka", "IS1998185026"),
        Ref("Freyja", "Prestsbakka", "IS1993285026"),
        Sex.GELDING,
        image="kjarkur",
    ),
    Horse(
        tb("Blesi", "IS2013185260"),
        Category.RIDING_HORSE,
        Ref("Konsert", "Korpu", "IS2005101001"),
        tb("Lyfting", "IS2006285260"),
        Sex.GELDING,
        image="blesi",
    ),
    Horse(
        tb("Baldur", "IS2015185260"),
        Category.RIDING_HORSE,
        Ref("Arður", "Brautarholti", "IS2001137637"),
        tb("Lyfting", "IS2006285260"),
        Sex.GELDING,
        image="baldur",
    ),
    Horse(
        tb("Blær", "IS2019185260"),
        Category.RIDING_HORSE,
        Ref("Konsert", "Hofi", "IS2010156107"),
        tb("Lyfting", "IS2006285260"),
        Sex.GELDING,
        image="blaer",
    ),
    Horse(
        tb("Askur", "IS2018185260"),
        Category.RIDING_HORSE,
        Ref("Apollo", "Haukholtum", "IS2012188158"),
        tb("Þokkadís", "IS2008285260"),
        Sex.GELDING,
        image="askur",
    ),
    Horse(
        tb("Svartstjarna", "IS2000285260"),
        Category.RIDING_HORSE,
        Ref("Ásaþór", "Feti", "IS1991186919"),
        Ref("Mósa", "Teigi II", "IS1987284810"),
        Sex.MARE,
        image="svartstjarna",
    ),
)

HORSES: tuple[Horse, ...] = (LYFTING, FREYJA, THOKKADIS, DOGUN, GNA, *YOUNG, *RIDING)

# Gallery photos live in images/gallery/NN.webp (full) + NN_thumb.webp (grid thumbnail).
GALLERY_COUNT = 46

# Placeholder names used in the source for foals not yet named.
UNNAMED_MARKERS = frozenset({"Nn", "Nm"})


def by_category(category: Category) -> list[Horse]:
    return [h for h in HORSES if h.category == category]


def featured() -> list[Horse]:
    return [h for h in HORSES if h.featured]
