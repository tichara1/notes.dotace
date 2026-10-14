# Struktura repa: podklady → model → vyřizování

**Datum:** 2026-10-14
**Stav:** navrženo (PR #1)
**Nahrazuje strukturu z:** `2026-05-31-rekonstrukce-dotace-struktura-design.md`

## Cíl

Radek chce do repa postupně dávat podklady o domě, vyúčtování elektřiny a plynu
a navržená opatření (výstup Fáze 0 od Consultory) a s AI z nich modelovat úspory
a návratnost, vybírat firmy podle recenzí a volit materiály.

## Rozhodnutí

- **Podklady mají vlastní sekce** hned za Přehledem (02 Dům, 03 Energie,
  04 Opatření), aby šly vyplňovat nezávisle a AI je našla na jednom místě.
- **Model (05)** jen čte podklady a drží předpoklady + výsledky s datem výpočtu.
  Stránka *Měsíční platby* se přesunula z Dotací sem.
- Původní sekce se posunuly: Dotace 02→06, Specialisté 03→07, Realizace 04→08,
  Rozpočet 05→09, Dokumenty 06→10 (přes `git mv`, odkazy přepsané).
- Data se píšou jako **Markdown tabulky** (čitelné na webu i pro AI), žádné CSV/skripty.
- **Soukromí:** web je veřejný → surové soubory (PDF vyúčtování, skeny, fotky) jen
  v lokální `_soukrome/` (v `.gitignore`, Jekyll ji navíc ignoruje díky `_`).
- Každá sekce má `index.md` = „README" sekce: co do ní patří a jak doplňovat.
- Neaktuální obsah jde do `archiv/` (přesouvá se, nemaže).

## Struktura

```
01-prehled/      cíl a rozsah, harmonogram
02-dum/          parametry domu, okna a dveře
03-energie/      vyúčtování elektřiny a plynu
04-opatreni/     varianty opatření, materiály a výrobky
05-model/        předpoklady, úspory a návratnost, měsíční platby
06-dotace/       NZÚ přehled, závazné pokyny, podklady, financování
07-specialiste/  energetický specialista, Consultora — spolupráce
08-realizace/    firma vs sub, poptávky, srovnání nabídek, firmy podle recenzí
09-rozpocet/     rozpočet
10-dokumenty/    deník a dokumenty
reserse-nzu-2026.md, archiv/, docs/, tools/
```
