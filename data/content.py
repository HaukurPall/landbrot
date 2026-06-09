"""Bilingual UI strings and prose for landbrot.is.

Prose paragraphs are transcribed verbatim from Arnar's source documents (one Icelandic, one
German). Short UI labels use clean, idiomatic wording; obvious machine-translation slips in
the German source (``Vatter``→Vater, ``Pferde hacken``→Reitpferde, ``Zuchterge°°bnis``→
Zuchtergebnis, ``Gelding``→Wallach, ``Funfgang``→Fünfgang, ``Jungendklasse``→Jugendklasse)
are corrected here so there is a single, consistent place for every translation.
"""

from __future__ import annotations

from data.horses import bl

LANGS: tuple[str, ...] = ("is", "de")

SITE_NAME = "Landbrot"
TAGLINE = bl("Hrossaræktarbú", "Islandpferdezucht")

# Ordered navigation. `file` is the output filename, shared between / (IS) and /de/ (DE).
PAGES: list[dict] = [
    {
        "key": "home",
        "file": "index.html",
        "nav": bl("Forsíða", "Startseite"),
        "title": bl("Landbrot – Hrossaræktarbú", "Landbrot – Islandpferdezucht"),
        "desc": bl(
            "Landbrot ehf. hrossaræktarbú – ræktun íslenskra hrossa kennd við Þykkvabæ I í Landbroti.",
            "Landbrot ehf. – Zucht von Islandpferden aus Þykkvabær I in Landbrot, Island.",
        ),
    },
    {
        "key": "about",
        "file": "um-okkur.html",
        "nav": bl("Um okkur", "Über uns"),
        "title": bl("Um okkur – Landbrot", "Über uns – Landbrot"),
        "desc": bl(
            "Um Landbrot ehf. hrossaræktarbú – Arnar Bjarnason og Anna María Pétursdóttir.",
            "Über Landbrot ehf. – Arnar Bjarnason und Anna María Pétursdóttir.",
        ),
    },
    {
        "key": "breeding",
        "file": "raektunarhross.html",
        "nav": bl("Ræktunarhryssur", "Zuchtstuten"),
        "title": bl("Ræktunarhryssur – Landbrot", "Zuchtstuten – Landbrot"),
        "desc": bl(
            "Ræktunarhryssur Landbrots: Lyfting, Þokkadís, Dögun og Gná frá Þykkvabæ I.",
            "Die Zuchtstuten von Landbrot: Lyfting, Þokkadís, Dögun und Gná von Þykkvabær I.",
        ),
    },
    {
        "key": "young",
        "file": "unghross.html",
        "nav": bl("Unghross", "Jungpferde"),
        "title": bl("Unghross – Landbrot", "Jungpferde – Landbrot"),
        "desc": bl(
            "Unghross frá Þykkvabæ I – unghryssur og unghestar í ræktun Landbrots.",
            "Jungpferde von Þykkvabær I – junge Stuten und Hengste aus der Zucht von Landbrot.",
        ),
    },
    {
        "key": "riding",
        "file": "reidhross.html",
        "nav": bl("Reiðhross", "Reitpferde"),
        "title": bl("Reiðhross – Landbrot", "Reitpferde – Landbrot"),
        "desc": bl(
            "Reiðhrossin okkar hjá Landbrot.",
            "Unsere Reitpferde bei Landbrot.",
        ),
    },
    {
        "key": "contact",
        "file": "hafa-samband.html",
        "nav": bl("Hafa samband", "Kontakt"),
        "title": bl("Hafa samband – Landbrot", "Kontakt – Landbrot"),
        "desc": bl(
            "Hafðu samband við Landbrot ehf. hrossaræktarbú.",
            "Kontaktieren Sie Landbrot ehf.",
        ),
    },
    {
        "key": "gallery",
        "file": "myndabanki.html",
        "nav": bl("Myndabanki", "Bildergalerie"),
        "title": bl("Myndabanki – Landbrot", "Bildergalerie – Landbrot"),
        "desc": bl(
            "Myndir frá Landbrot ehf. hrossaræktarbúi.",
            "Bilder von Landbrot ehf.",
        ),
    },
]

# Prose, verbatim from the source documents.
PROSE = {
    "intro": bl(
        "Landbrot ehf. hrossaræktarbú er félag sem stofnað var árið 2009 utan um hestaeign og "
        "hrossarækt Arnars Bjarnasonar og Önnu Maríu Pétursdóttur sem búsett eru á Seltjarnarnesi. "
        "Hrossin okkar eru kennd við Þykkvabæ I í Landbroti í Vestur-Skaftafellssýslu.",
        "Landbrot ehf. ist ein 2009 gegründetes Unternehmen, das sich um die Pferdehaltung und "
        "-zucht von Arnar Bjarnason und Anna María Pétursdóttir in Seltjarnarnes dreht. Unsere "
        "Pferde sind nach Þykkvabær I. in Landbrot in Vestur-Skaftafellssýsla benannt.",
    ),
    "ancestry": bl(
        "Hrossarækt okkar byggir fyrst og fremst á tveimur ættmæðrum. Annarsvegar, 1. verðlauna "
        "hryssunni Freyju frá Prestsbakka (IS1993285026), dóttur heiðursverðlaunahryssunnar Gyðju "
        "frá Gerðum (IS1982286002) og stóðhestsins Gnýs frá Hrepphólum (IS1988188170) og hinsvegar "
        "1. verðlauna hryssunni Lyftingu frá Þykkvabæ (IS2006285260) sem er undan Jörp frá Þykkvabæ "
        "(IS1996285260) og Þokka frá Kýrholti (IS1997158430).",
        "Unsere Pferdezucht basiert hauptsächlich auf zwei Stuten. Einerseits die 1. Preisstute "
        "Freyja frá Prestsbakka (IS1993285026), Tochter der Ehrenpreisstute Gyðja frá Gerðum "
        "(IS1982286002) und des Hengstes Gnýr frá Hrepphólum (IS1988188170) und andererseits die "
        "1. Preisstute Lyfting frá Þykkvabæ (IS2006285260), ein Nachkomme von Jörp frá Þykkvabæ "
        "(IS1996285260) und Þokki frá Kýrholti (IS1997158430).",
    ),
    "goals": bl(
        "Ræktunarmarkmið okkar er að rækta léttstíg hross sem eru sjálfberandi í reið, með allar "
        "gangtegundir og góðan vilja. Hvað varðar byggingu hrossa, þá leggjum við mesta áherslu á "
        "háttsettan háls og herðar, öflugt bak og lend og gott samræmi. Varðandi eiginleika þá er "
        "ræktunarmarkmið okkar að rækta alhliðageng hross, með mjúkt tölt og afburða geðslag.",
        "Unser Zuchtziel ist es, leichtfüßige, selbsttragende Pferde mit allen Gangarten und gutem "
        "Willen zu züchten. Bei der Pferdezucht legen wir größten Wert auf einen hohen Hals und "
        "eine starke Schulterpartie, einen kräftigen Rücken und eine ausgeprägte Lende sowie eine "
        "harmonische Körperhaltung. Unser Zuchtziel sind vielseitige Pferde mit einem weichen Tölt "
        "und einem ausgezeichneten Temperament.",
    ),
}

# Contact people, in source order.
CONTACT = [
    {"name": "Arnar Bjarnason", "phone": "+354 842 5000", "email": "arnar@reykjavik-capital.is"},
    {
        "name": "Anna María Pétursdóttir",
        "phone": "+354 895 5299",
        "email": "amp@reykjavik-capital.is",
    },
]

# Short UI labels. Accessed in templates as t.<key> after localizing for one language.
LABELS = {
    "skip_to_content": bl("Beint í efni", "Zum Inhalt springen"),
    "menu": bl("Valmynd", "Menü"),
    "sire": bl("Faðir", "Vater"),
    "dam": bl("Móðir", "Mutter"),
    "connective": bl("frá", "von"),
    "unnamed": bl("Ónefnt", "Unbenannt"),
    "sex_mare": bl("Hryssa", "Stute"),
    "sex_stallion": bl("Hestur", "Hengst"),
    "sex_gelding": bl("Geldingur", "Wallach"),
    "score_total": bl("Aðaleinkunn", "Gesamtnote"),
    "score_conformation": bl("Bygging", "Exterieur"),
    "score_rideability": bl("Hæfileikar", "Reiteigenschaften"),
    "score_total_short": bl("Aðal.", "Ges."),
    "score_conformation_short": bl("Bygg.", "Ext."),
    "score_rideability_short": bl("Hæf.", "Reit."),
    "assessment_line": bl(
        "Hæsti kynbótadómur {age} vetra árið {year}",
        "Höchstes Zuchtergebnis mit {age} Jahren im Jahr {year}",
    ),
    "results_heading": bl("Keppnisárangur", "Wettbewerbsergebnisse"),
    "offspring_heading": bl("Afkvæmi", "Nachkommen"),
    "col_name": bl("Nafn", "Name"),
    "col_sex": bl("Kyn", "Geschlecht"),
    "col_rider": bl("Knapi", "Reiter"),
    "col_discipline": bl("Grein", "Disziplin"),
    "col_class": bl("Flokkur", "Klasse"),
    "col_round": bl("Umferð", "Runde"),
    "col_score": bl("Einkunn", "Note"),
    "col_rank": bl("Sæti", "Platz"),
    "foundation_heading": bl("Ættmæður okkar", "Unsere Stammstuten"),
    "young_mares_heading": bl("Unghryssur", "Junge Stuten"),
    "young_males_heading": bl("Unghestar", "Junge Pferde"),
    "contact_subheading": bl("Nánari upplýsingar", "Weitere Informationen"),
    "contact_phone": bl("Sími", "Telefon"),
    "contact_email": bl("Netfang", "E-Mail"),
    "lang_is": bl("Íslenska", "Isländisch"),
    "lang_de": bl("Þýska", "Deutsch"),
    "footer": bl(
        "Landbrot ehf. — Arnar Bjarnason og Anna María Pétursdóttir",
        "Landbrot ehf. — Arnar Bjarnason und Anna María Pétursdóttir",
    ),
}


def localize(value: dict[str, str] | str, lang: str) -> str:
    """Pick the `lang` variant of a bilingual dict, or pass through a plain string."""
    if isinstance(value, str):
        return value
    return value[lang]
