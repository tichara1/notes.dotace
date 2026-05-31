# Struktura poznámek: Rekonstrukce domu + dotace NZÚ 2026+

**Datum:** 2026-05-31
**Stav:** schváleno (návrh)

## Cíl

Vytvořit přehlednou strukturu Markdown poznámek pro plánování a realizaci
rekonstrukce rodinného domu s dotací **Nová zelená úsporám 2026+** (vyhlášena
28.5.2026). Repo se publikuje jako GitHub Pages a sdílí s přítelkyní.

Uživatel je na úplném začátku — nic není rozjeté. Struktura musí pomoct
naplánovat rozsah, vybrat financování, oslovit energetického specialistu,
rozhodnout způsob realizace a posbírat podklady.

## Klíčová fakta o NZÚ 2026+ (formují strukturu)

- Místo přímé dotace pro většinu žadatelů **bezúročný úvěr** (100 tis.–2 mil.
  Kč, úroky hradí fond) → potřeba sekce porovnání úvěr vs. přímá dotace.
- **Povinný renovační pas / energetický posudek** → hlavní podklad.
- Síť **certifikovaných energetických specialistů** → „dotační specialisti",
  které chce uživatel oslovit; jejich zapojení je nově prakticky povinné.
- **NZÚ Light** = přímá dotace pro nízkopříjmové; ostatní žadatelé = úvěr.

Zdroje: MŽP (NZÚ 2026+), ČESKÉSTAVBY (NZÚ 2026 rodinné domy).

## Rozhodnutí

- **Jazyk obsahu:** čeština.
- **Publikace:** GitHub Pages s tématem `just-the-docs` přes `remote_theme`
  (boční menu + vyhledávání, žádné CI/lokální build na straně uživatele).
- **Formát:** čisté `.md` soubory, každý s připravenou kostrou (nadpisy,
  checklisty, prázdné tabulky) k doplňování.

## Struktura repa

```
notes.dotace/
├── README.md                      # jak repo používat (pro oba)
├── _config.yml                    # remote_theme just-the-docs, název webu
├── index.md                       # úvodní rozcestník
├── 01-prehled/
│   ├── cil-a-rozsah.md            # co rekonstruujeme, priority, must-have vs nice-to-have
│   └── harmonogram.md             # časová osa a milníky
├── 02-dotace/
│   ├── nzu-2026-prehled.md        # na co dosáhneme, kolik, podmínky
│   ├── podklady-checklist.md      # renovační pas, posudek, doklady — co a kdy
│   └── financovani.md             # přímá dotace vs bezúročný úvěr
├── 03-specialiste/
│   ├── energeticky-specialista.md # role, jak vybrat, co od nás potřebuje
│   └── oslovene-kontakty.md       # koho jsme oslovili, stav, poznámky
├── 04-realizace/
│   ├── firma-vs-subdodavatele.md  # rozhodovací matice
│   ├── poptavky.md                # koho oslovit, stav poptávky
│   └── nabidky-srovnani.md        # tabulka srovnání nabídek
├── 05-rozpocet/
│   └── rozpocet.md                # odhad nákladů, dotace/úvěr, vlastní zdroje
└── 06-dokumenty/
    └── deniky-a-dokumenty.md      # deník jednání + odkazy na dokumenty
```

`just-the-docs` řadí stránky podle `nav_order` ve frontmatteru; číslování složek
drží i přirozené pořadí v Gitu. Každá stránka dostane frontmatter s `title`,
`nav_order` a (u podstránek) `parent`.

## Mimo rozsah (YAGNI)

- Bez vlastního CI/buildu, bez custom CSS.
- Bez sekce stavebního úřadu/povolení zatím (lze doplnit, pokud rekonstrukce
  bude vyžadovat stavební povolení).
- Žádná automatizace, skripty ani generování obsahu.

## Úspěch

- Repo lze pushnout na GitHub, zapnout Pages a web se vykreslí s bočním menu.
- Uživatel může rovnou psát konkrétní poznámky do připravených kostech.
