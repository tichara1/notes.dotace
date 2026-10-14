---
title: Energie
nav_order: 3
has_children: true
---

# Energie — spotřeba a vyúčtování

**Co sem patří:** skutečná spotřeba a ceny elektřiny a plynu z vyúčtování — po
obdobích, s jednotkovou cenou a tarifem. Je to hlavní vstup pro
[model úspor](../05-model/index.html): bez skutečné spotřeby nejde spočítat, kolik
opatření ušetří.

- [Vyúčtování elektřiny a plynu](vyuctovani.html) — souhrn, tabulky po obdobích, roční přehled
  a ceny pro model; pod ním **13 přepisů jednotlivých vyúčtování** (elektřina 2021–2026, plyn 2021–2026)

**Ve zkratce (poslední rok):** elektřina **6 338 kWh / ≈ 42 600 Kč** (≈ 3 550 Kč/měs.),
plyn **37 388 kWh / ≈ 64 850 Kč** (≈ 5 400 Kč/měs.), dohromady **≈ 107 000 Kč/rok**.
Obojí innogy, produkt Optimal 36 s fixací do **15. 11. 2027**.

## Jak doplňovat

- Každé nové vyúčtování = **nový řádek** v tabulce (období, spotřeba, částka) a nová stránka
  v `03-energie/vyuctovani/` pojmenovaná stejně jako PDF:
  `<elektrina|plyn>_<od>_<do>_<dodavatel>_<radne|mimoradne>-vyuctovani`.
- Jednotkovou cenu počítej jako *celková částka ÷ spotřeba* (vč. DPH a stálých plateb),
  ať jde porovnávat napříč obdobími.
- Pokud máš i měsíční odečty nebo data z chytrého elektroměru, přidej je jako další tabulku.

> 🔒 **Web je veřejný.** PDF vyúčtování obsahují jméno, adresu a číslo odběrného
> místa → do repa je **nenahrávej**, ulož je do `_soukrome/` (v `.gitignore`).
> Sem přepiš jen čísla. Přejmenované originály jsou ve sdílené složce projektu `vyuctovani/`.
