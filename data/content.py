"""Localized UI strings and prose for landbrot.is (Icelandic, German, English).

Prose paragraphs are transcribed verbatim from Arnar's source documents (Icelandic and
German); the English prose was translated by us and is awaiting Arnar's review. Short UI
labels use clean, idiomatic wording; obvious machine-translation slips in the German source
(``Vatter``→Vater, ``Pferde hacken``→Reitpferde, ``Zuchterge°°bnis``→Zuchtergebnis,
``Gelding``→Wallach, ``Funfgang``→Fünfgang, ``Jungendklasse``→Jugendklasse) are corrected
here so there is a single, consistent place for every translation.

Horse names keep the Icelandic connective "frá" in English — the international convention
for Icelandic horses (WorldFengur/FEIF usage) — while German uses "von" as in the source.
"""

from __future__ import annotations

from data.horses import bl

LANGS: tuple[str, ...] = ("is", "de", "en")

SITE_NAME = "Landbrot"
TAGLINE = bl("Hrossaræktarbú", "Islandpferdezucht", "Horse Breeding Farm")

# Ordered navigation. `file` is the output filename, shared between / (IS), /de/ and /en/.
# `nav_divider` draws a separator before the item; `in_nav: False` keeps a page out of the
# top navigation (it is linked from the footer instead).
PAGES: list[dict] = [
    {
        "key": "home",
        "file": "index.html",
        "nav": bl("Forsíða", "Startseite", "Home"),
        "title": bl(
            "Landbrot – Hrossaræktarbú",
            "Landbrot – Islandpferdezucht",
            "Landbrot – Horse Breeding Farm",
        ),
        "desc": bl(
            "Landbrot ehf. hrossaræktarbú – ræktun íslenskra hrossa kennd við Þykkvabæ I í Landbroti.",
            "Landbrot ehf. – Zucht von Islandpferden aus Þykkvabær I in Landbrot, Island.",
            "Landbrot ehf. – breeding Icelandic horses named after Þykkvabær I in Landbrot, Iceland.",
        ),
    },
    {
        "key": "breeding",
        "file": "raektunarhross.html",
        "nav": bl("Ræktunarhryssur", "Zuchtstuten", "Breeding mares"),
        "title": bl(
            "Ræktunarhryssur – Landbrot",
            "Zuchtstuten – Landbrot",
            "Breeding mares – Landbrot",
        ),
        "desc": bl(
            "Ræktunarhryssur Landbrots: Lyfting, Þokkadís, Dögun og Gná frá Þykkvabæ I.",
            "Die Zuchtstuten von Landbrot: Lyfting, Þokkadís, Dögun und Gná von Þykkvabær I.",
            "The breeding mares of Landbrot: Lyfting, Þokkadís, Dögun and Gná frá Þykkvabær I.",
        ),
    },
    {
        "key": "young",
        "file": "unghross.html",
        "nav": bl("Unghross", "Jungpferde", "Young horses"),
        "title": bl("Unghross – Landbrot", "Jungpferde – Landbrot", "Young horses – Landbrot"),
        "desc": bl(
            "Unghross frá Þykkvabæ I – unghryssur og unghestar í ræktun Landbrots.",
            "Jungpferde von Þykkvabær I – junge Stuten und Hengste aus der Zucht von Landbrot.",
            "Young horses from Þykkvabær I – young mares and colts bred by Landbrot.",
        ),
    },
    {
        "key": "riding",
        "file": "reidhross.html",
        "nav": bl("Reiðhross", "Reitpferde", "Riding horses"),
        "title": bl("Reiðhross – Landbrot", "Reitpferde – Landbrot", "Riding horses – Landbrot"),
        "desc": bl(
            "Reiðhrossin okkar hjá Landbrot.",
            "Unsere Reitpferde bei Landbrot.",
            "Our riding horses at Landbrot.",
        ),
    },
    {
        "key": "gallery",
        "file": "myndabanki.html",
        "nav": bl("Myndabanki", "Bildergalerie", "Gallery"),
        "title": bl("Myndabanki – Landbrot", "Bildergalerie – Landbrot", "Gallery – Landbrot"),
        "desc": bl(
            "Myndir frá Landbrot ehf. hrossaræktarbúi.",
            "Bilder von Landbrot ehf.",
            "Photos from Landbrot ehf.",
        ),
    },
    {
        "key": "about",
        "file": "um-okkur.html",
        "nav": bl("Um okkur", "Über uns", "About us"),
        "nav_divider": True,
        "title": bl("Um okkur – Landbrot", "Über uns – Landbrot", "About us – Landbrot"),
        "desc": bl(
            "Um Landbrot ehf. hrossaræktarbú – Arnar Bjarnason og Anna María Pétursdóttir.",
            "Über Landbrot ehf. – Arnar Bjarnason und Anna María Pétursdóttir.",
            "About Landbrot ehf. – Arnar Bjarnason and Anna María Pétursdóttir.",
        ),
    },
    {
        "key": "contact",
        "file": "hafa-samband.html",
        "nav": bl("Hafa samband", "Kontakt", "Contact"),
        "in_nav": False,
        "title": bl("Hafa samband – Landbrot", "Kontakt – Landbrot", "Contact – Landbrot"),
        "desc": bl(
            "Hafðu samband við Landbrot ehf. hrossaræktarbú.",
            "Kontaktieren Sie Landbrot ehf.",
            "Get in touch with Landbrot ehf.",
        ),
    },
]

# Prose. IS and DE are verbatim from the source documents; EN is our translation,
# pending Arnar's review.
PROSE = {
    "intro": bl(
        "Landbrot ehf. hrossaræktarbú er félag sem stofnað var árið 2009 utan um hestaeign og "
        "hrossarækt Arnars Bjarnasonar og Önnu Maríu Pétursdóttur sem búsett eru á Seltjarnarnesi. "
        "Hrossin okkar eru kennd við Þykkvabæ I í Landbroti í Vestur-Skaftafellssýslu.",
        "Landbrot ehf. ist ein 2009 gegründetes Unternehmen, das sich um die Pferdehaltung und "
        "-zucht von Arnar Bjarnason und Anna María Pétursdóttir in Seltjarnarnes dreht. Unsere "
        "Pferde sind nach Þykkvabær I. in Landbrot in Vestur-Skaftafellssýsla benannt.",
        "Landbrot ehf. is a horse breeding farm founded in 2009 around the horses and breeding "
        "of Arnar Bjarnason and Anna María Pétursdóttir, who live in Seltjarnarnes, Iceland. "
        "Our horses are named after Þykkvabær I in Landbrot, Vestur-Skaftafellssýsla.",
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
        "Our breeding is first and foremost built on two foundation mares. On the one hand, the "
        "first-prize mare Freyja frá Prestsbakka (IS1993285026), daughter of the honour-prize mare "
        "Gyðja frá Gerðum (IS1982286002) and the stallion Gnýr frá Hrepphólum (IS1988188170), and "
        "on the other the first-prize mare Lyfting frá Þykkvabæ (IS2006285260), out of Jörp frá "
        "Þykkvabæ (IS1996285260) by Þokki frá Kýrholti (IS1997158430).",
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
        "Our goal is to breed light-footed horses that carry themselves under the rider, with all "
        "gaits and a good, willing temperament. In conformation we place the greatest emphasis on "
        "a high-set neck and withers, a strong back and croup, and good overall proportions. As "
        "for abilities, our aim is to breed versatile all-round horses with a soft tölt and an "
        "outstanding character.",
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
    "skip_to_content": bl("Beint í efni", "Zum Inhalt springen", "Skip to content"),
    "menu": bl("Valmynd", "Menü", "Menu"),
    "sire": bl("Faðir", "Vater", "Sire"),
    "dam": bl("Móðir", "Mutter", "Dam"),
    "connective": bl("frá", "von", "frá"),
    "unnamed": bl("Ónefnt", "Unbenannt", "Unnamed"),
    "sex_mare": bl("Hryssa", "Stute", "Mare"),
    "sex_stallion": bl("Hestur", "Hengst", "Stallion"),
    "sex_gelding": bl("Geldingur", "Wallach", "Gelding"),
    "score_total": bl("Aðaleinkunn", "Gesamtnote", "Total score"),
    "score_conformation": bl("Bygging", "Exterieur", "Conformation"),
    "score_rideability": bl("Hæfileikar", "Reiteigenschaften", "Ridden abilities"),
    "score_total_short": bl("Aðal.", "Ges.", "Total"),
    "score_conformation_short": bl("Bygg.", "Ext.", "Conf."),
    "score_rideability_short": bl("Hæf.", "Reit.", "Ridden"),
    "assessment_line": bl(
        "Hæsti kynbótadómur {age} vetra árið {year}",
        "Höchstes Zuchtergebnis mit {age} Jahren im Jahr {year}",
        "Highest breeding assessment as a {age}-year-old in {year}",
    ),
    "results_heading": bl("Keppnisárangur", "Wettbewerbsergebnisse", "Competition results"),
    "offspring_heading": bl("Afkvæmi", "Nachkommen", "Offspring"),
    "col_name": bl("Nafn", "Name", "Name"),
    "col_sex": bl("Kyn", "Geschlecht", "Sex"),
    "col_rider": bl("Knapi", "Reiter", "Rider"),
    "col_discipline": bl("Grein", "Disziplin", "Discipline"),
    "col_class": bl("Flokkur", "Klasse", "Class"),
    "col_round": bl("Umferð", "Runde", "Round"),
    "col_score": bl("Einkunn", "Note", "Score"),
    "col_rank": bl("Sæti", "Platz", "Rank"),
    "foundation_heading": bl("Ættmæður okkar", "Unsere Stammstuten", "Our foundation mares"),
    "young_mares_heading": bl("Unghryssur", "Junge Stuten", "Young mares"),
    "young_males_heading": bl("Unghestar", "Junge Pferde", "Young colts"),
    "contact_subheading": bl("Nánari upplýsingar", "Weitere Informationen", "Further information"),
    "contact_phone": bl("Sími", "Telefon", "Phone"),
    "contact_email": bl("Netfang", "E-Mail", "Email"),
    "lang_is": bl("Íslenska", "Isländisch", "Icelandic"),
    "lang_de": bl("Þýska", "Deutsch", "German"),
    "lang_en": bl("Enska", "Englisch", "English"),
    "footer": bl(
        "Landbrot ehf. — Arnar Bjarnason og Anna María Pétursdóttir",
        "Landbrot ehf. — Arnar Bjarnason und Anna María Pétursdóttir",
        "Landbrot ehf. — Arnar Bjarnason and Anna María Pétursdóttir",
    ),
}


def localize(value: dict[str, str] | str, lang: str) -> str:
    """Pick the `lang` variant of a localized dict, or pass through a plain string."""
    if isinstance(value, str):
        return value
    return value[lang]
