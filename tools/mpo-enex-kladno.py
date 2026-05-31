#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mpo-enex-kladno.py

Stáhne z OFICIÁLNÍHO rejstříku energetických specialistů MPO-ENEX
(https://www.mpo-enex.cz/experti/ExpertList.aspx) seznam držitelů oprávnění
ke zpracování PENB (Průkaz energetické náročnosti budov) ve Středočeském kraji,
vyfiltruje obce okresu Kladno / v dojezdu Dřetovic, u každého stáhne z detailu
kontaktní údaje (telefon, e-mail, adresa, platnost) a přidá ověřovací odkazy
(Google Maps / Firmy.cz / Google) pro ruční prověření hodnocení.

ŽELEZNÉ PRAVIDLO: vypisují se POUZE data skutečně stažená z rejstříku.
Co se nepodaří získat, je označeno jako "nenalezeno". Nic se nevymýšlí.

Spuštění:   python tools/mpo-enex-kladno.py
Výstup:     03-specialiste/specialiste-kladno.md  (stránka webu, + výpis do konzole)

Jen standardní knihovna Pythonu (žádné závislosti) — repo je obsahové.
"""

import html
import re
import time
import urllib.parse
import urllib.request
from http.cookiejar import CookieJar
from datetime import date
from pathlib import Path

BASE = "https://www.mpo-enex.cz/experti/ExpertList.aspx"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) notes.dotace-research/1.0"

# Filtr formuláře: Kraj=Středočeský(11), Druh oprávnění=PENB(4), Třídění=Obec(3)
KRAJ_STREDOCESKY = "11"
TYP_PENB = "4"
TRID_OBEC = "3"

# Obce okresu Kladno + nejbližší dojezd Dřetovic (Dřetovice ~ 273 42, okr. Kladno).
# Filtruje se podle názvu obce NEBO podle prefixu PSČ (272/273/274 = okres Kladno).
OBEC_KEYWORDS = [
    "Dřetovice", "Kladno", "Kročehlavy", "Švermov", "Buštěhrad", "Stehelčeves",
    "Brandýsek", "Zákolany", "Koleč", "Kamenné Žehrovice", "Libušín", "Smečno",
    "Pchery", "Vinařice", "Slaný", "Velvary", "Zvoleněves", "Družec", "Unhošť",
    "Hostouň", "Kralupy", "Stochov", "Tuchlovice", "Velká Dobrá", "Lány",
    "Doksy", "Hřebeč", "Cvrčovice", "Knovíz", "Pchery", "Třebusice",
]
PSC_PREFIXES = ("272", "273", "274")  # okres Kladno


def fetch(url, data=None, opener=None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    # stránka je v UTF-8
    return raw.decode("utf-8", errors="replace")


def get_hidden(name, page):
    m = re.search(r'name="%s"[^>]*?value="([^"]*)"' % re.escape(name), page)
    return m.group(1) if m else ""


def hidden_fields(page):
    return {
        "__VIEWSTATE": get_hidden("__VIEWSTATE", page),
        "__VIEWSTATEGENERATOR": get_hidden("__VIEWSTATEGENERATOR", page),
        "__EVENTVALIDATION": get_hidden("__EVENTVALIDATION", page),
    }


def page_numbers(page):
    m = re.search(r'name="stranaNav".*?</select>', page, re.S)
    if not m:
        return [1]
    nums = [int(x) for x in re.findall(r'<option[^>]*value="(\d+)"', m.group(0))]
    return sorted(set(nums)) or [1]


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def parse_list(page):
    """Vrátí seznam dictů {idSpec, jmeno, obec, penb_platny} z výsledkové tabulky."""
    names = {}  # index -> (idSpec, jmeno)
    for m in re.finditer(
        r'id="zobrazeni_hpExp_(\d+)"\s+href="ExpertList\.aspx\?idSpec=(\d+)">([^<]+)</a>',
        page,
    ):
        idx, idspec, jmeno = m.group(1), m.group(2), html.unescape(m.group(3)).strip()
        names[idx] = (idspec, jmeno)

    obce = {}
    for m in re.finditer(r'id="zobrazeni_lObec_(\d+)">([^<]*)</span>', page):
        obce[m.group(1)] = html.unescape(m.group(2)).strip()

    penb = {}
    for m in re.finditer(r'id="zobrazeni_Image4_(\d+)"[^>]*alt="([^"]+)"', page):
        penb[m.group(1)] = html.unescape(m.group(2)).strip()

    out = []
    for idx, (idspec, jmeno) in names.items():
        out.append({
            "idSpec": idspec,
            "jmeno": jmeno,
            "obec": obce.get(idx, ""),
            "penb_platny": penb.get(idx, "?"),
        })
    return out


def is_near(obec):
    psc = re.search(r"\b(\d{3})\s?\d{2}\b", obec)
    if psc and psc.group(1) in PSC_PREFIXES:
        return True
    low = obec.lower()
    return any(k.lower() in low for k in OBEC_KEYWORDS)


def parse_detail(page):
    """Z detailu vytáhne dvojice klíč/hodnota z tabulky 'Kontaktní údaje'."""
    fields = {}
    for m in re.finditer(
        r"<td><span>(?:<b>)?(.*?)(?:</b>)?</span></td>\s*<td><span>(?:<b>)?(.*?)(?:</b>)?</span></td>",
        page, re.S,
    ):
        key = strip_tags(m.group(1))
        val = strip_tags(m.group(2))
        if key:
            fields[key] = val
    return fields


def verify_links(jmeno, obec):
    q_maps = urllib.parse.quote(f"{jmeno} {obec}")
    q_firmy = urllib.parse.quote(jmeno)
    q_goog = urllib.parse.quote(f"{jmeno} {obec} recenze hodnocení")
    return {
        "maps": f"https://www.google.com/maps/search/?api=1&query={q_maps}",
        "firmy": f"https://www.firmy.cz/?q={q_firmy}",
        "google": f"https://www.google.com/search?q={q_goog}",
    }


def main():
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    print("GET formuláře…")
    form = fetch(BASE, opener=opener)
    filtr = {
        "dlKraj": KRAJ_STREDOCESKY,
        "dlTyp": TYP_PENB,
        "dlTrid": TRID_OBEC,
    }
    payload = {**hidden_fields(form), **filtr, "hledat": "Vyhledat"}
    if not payload["__VIEWSTATE"]:
        raise SystemExit("CHYBA: nepodařilo se načíst __VIEWSTATE — změnila se struktura stránky?")

    print("POST filtru (Středočeský kraj + PENB)…")
    cur = fetch(BASE, data=urllib.parse.urlencode(payload).encode("utf-8"), opener=opener)

    vsichni = parse_list(cur)
    pages = page_numbers(cur)
    print(f"Stránek výsledků: {len(pages)} (po 100 záznamech)")

    # Projdi další stránky postbackem na 'stranaNav' (viewstate se obnovuje z poslední odpovědi).
    for p in pages:
        if p == 1:
            continue
        nav = {**hidden_fields(cur), **filtr, "stranaVel": "100",
               "__EVENTTARGET": "stranaNav", "__EVENTARGUMENT": "", "stranaNav": str(p)}
        cur = fetch(BASE, data=urllib.parse.urlencode(nav).encode("utf-8"), opener=opener)
        vsichni.extend(parse_list(cur))
        time.sleep(0.5)

    # Odstraň duplicity podle idSpec
    seen, uniq = set(), []
    for s in vsichni:
        if s["idSpec"] not in seen:
            seen.add(s["idSpec"])
            uniq.append(s)
    vsichni = uniq
    if not vsichni:
        raise SystemExit("CHYBA: výsledková tabulka prázdná — ověř strukturu/filtr.")
    print(f"Středočeský kraj – držitelů PENB nalezeno: {len(vsichni)}")

    blizko = [s for s in vsichni if is_near(s["obec"])]
    print(f"V okrese Kladno / dojezdu Dřetovic: {len(blizko)}")

    # Detaily (kontakty) — slušně, s krátkou prodlevou.
    for s in blizko:
        try:
            det = fetch(f"{BASE}?idSpec={s['idSpec']}", opener=opener)
            f = parse_detail(det)
            s["telefon"] = f.get("Telefon", "") or "nenalezeno"
            s["email"] = f.get("E-mail", "") or "nenalezeno"
            s["adresa"] = f.get("Adresa", s["obec"]) or s["obec"]
            s["platnost"] = f.get("Platnost oprávnění", "nenalezeno")
        except Exception as e:  # noqa
            s["telefon"] = s["email"] = "chyba detailu"
            s["adresa"] = s["obec"]
            s["platnost"] = "?"
            print(f"  ! detail {s['idSpec']} selhal: {e}")
        time.sleep(0.6)

    # Seřadit podle obce, pak jména
    blizko.sort(key=lambda x: (x["obec"], x["jmeno"]))

    out = Path(__file__).resolve().parent.parent / "03-specialiste" / "specialiste-kladno.md"
    lines = []
    # just-the-docs front matter (stránka sekce „Specialisté")
    lines.append("---")
    lines.append("title: Specialisté PENB (okres Kladno)")
    lines.append("parent: Specialisté")
    lines.append("nav_order: 3")
    lines.append("---")
    lines.append("")
    lines.append("# Energetičtí specialisté (PENB) – okres Kladno / dojezd Dřetovic")
    lines.append("")
    lines.append(f"> Zdroj: oficiální rejstřík **MPO-ENEX** ({BASE}), filtr Středočeský kraj + oprávnění PENB.")
    lines.append(f"> Staženo: **{date.today().isoformat()}**. Středočeský kraj celkem: {len(vsichni)} držitelů PENB; "
                 f"v okrese Kladno / dojezdu Dřetovic: **{len(blizko)}**.")
    lines.append("> Jména, telefony, e-maily a platnost jsou z rejstříku (ověřitelné). "
                 "Hodnocení rejstřík neobsahuje → ověřte přes odkazy ve sloupci *Ověření hodnocení*.")
    lines.append("")
    lines.append("| Jméno / firma | Adresa | Platnost PENB | Telefon | E-mail | Detail v rejstříku | Ověření hodnocení |")
    lines.append("|---|---|---|---|---|---|---|")
    for s in blizko:
        v = verify_links(s["jmeno"], s["obec"])
        detail = f"https://www.mpo-enex.cz/experti/ExpertList.aspx?idSpec={s['idSpec']}"
        overeni = f"[Maps]({v['maps']}) · [Firmy.cz]({v['firmy']}) · [Google]({v['google']})"
        lines.append(
            f"| {s['jmeno']} | {s.get('adresa','')} | {s.get('platnost','?')} | "
            f"{s.get('telefon','?')} | {s.get('email','?')} | [detail]({detail}) | {overeni} |"
        )
    lines.append("")
    lines.append("> Pozn.: „nenalezeno“ = údaj v rejstříku chybí. Hodnocení (hvězdy/recenze) "
                 "ověřte ručně přes odkazy; rejstřík MPO je autoritativní pro platnost oprávnění.")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Uloženo: {out}  ({len(blizko)} záznamů)")


if __name__ == "__main__":
    main()
