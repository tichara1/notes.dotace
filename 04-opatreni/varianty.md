---
title: Varianty opatření
parent: Opatření
nav_order: 1
---

# Varianty opatření

> ✅ **Výstup Fáze 0 dorazil 15. 10. 2026** (Consultora, Ing. Vitouš). Originální PDF nejsou v repu
> (obsahují adresu), shrnutí níže. Dopad na náklady a úspory →
> [Úspory a návratnost](../05-model/navratnost.html).

## Závěr Fáze 0

- Budova splní podmínky **NZÚ — KOMPLEX jen HRANIČNĚ**, a to jen při **plném rozsahu**:
  zateplení fasády + výměna oken a vchodových dveří + FVE s baterií (obnovitelný zdroj je podmínka).
- **Varianta bez výměny oken se neuvažuje** — bez oken podmínky nesplní.
- Střecha, strop pod půdou a podlaha se **nezateplují** (0 m² v kalkulaci).
- **Venkovní stínění** je volitelné, z úvěru 3 000 Kč/m² stíněného okna.
- Předpokládaný úvěr **1 830 750 Kč** (= maximální způsobilé výdaje). Čerpá se jen na **přímé
  realizační náklady** (služby Consultory ne).
- Při změně tloušťky, materiálu nebo výrobku je nutné ji s Consultorou odsouhlasit **před podpisem
  smlouvy na Fáze 1–4** (výstup Fáze 0 se stává její přílohou).

## Navržená opatření

| Opatření | Rozsah | Požadovaný parametr | Z úvěru (sazba) | Max. z úvěru (Kč) |
|----------|-------:|---------------------|----------------:|------------------:|
| Zateplení obvodových stěn (ETICS) | 182,7 m² | bílý EPS **200 mm, λD ≤ 0,039** → U = 0,15 W/m²K | 3 500 Kč/m² | 639 450 |
| Výměna oken a vchodových dveří | 53,3 m² (okna 49,4 + dveře 3,9) | okna **Uw ≤ 0,90**, dveře **Ud ≤ 1,0**, g = 0,50; montáž dle ČSN 74 6077 | 12 000 Kč/m² | 639 600 |
| Venkovní stínění (volitelné) | 49,4 m² (všechna okna) | pohyblivé lamely, ruční nebo inteligentní ovládání z interiéru | 3 000 Kč/m² | 148 200 |
| FVE + baterie | 10 kWp + ≥ 10 kWh | měnič ≥ 95 % (hybrid ≥ 92 %), moduly ≥ 18 % | strop 400 000 | 400 000 |
| Zateplení podlahy na terénu | 0 m² | — | 5 000 Kč/m² | 0 |
| Zateplení ostatních konstrukcí, stropy | 0 m² | — | 2 000 Kč/m² | 0 |
| Wallbox | 0 | — | — | 0 |
| **Celkem** | | | | **1 830 750** |

> ⚠️ Součet řádků dává **1 827 250 Kč**, dokument uvádí 1 830 750 Kč (rozdíl 3 500 Kč = 1 m² stěny).
> Úvěr navíc **nesmí přesáhnout faktury** u každého opatření: plná částka vyjde jen při ceně fasády
> ≥ 3 500 Kč/m² a oken ≥ 12 000 Kč/m². Při tržních cenách vychází úvěr nižší (model: ≈ 1,42 mil. bez
> stínění) → [Úspory a návratnost](../05-model/navratnost.html).

## Skladby konstrukcí (navrhovaný stav)

| Konstrukce | Skladba (od interiéru) | U (W/m²K) | Mění se? |
|------------|------------------------|----------:|----------|
| S01 obvodová stěna | omítka + Porotherm 40 P+D (λ 0,174) + omítka + EPS 70F 200 mm + ETICS | **0,15** | ✅ zateplení |
| S02 stěna k nevytápěnému prostoru | Porotherm 40 P+D + omítky | 0,44 | ne |
| S03 stěna k nevytápěné půdě | Porotherm 14 P+D + omítky | **1,3** | ne |
| S04 stěna k nevytápěné půdě | Porotherm 11,5 P+D + omítky | **1,7** | ne |
| STR šikmá střecha / ST strop pod půdou | SDK + minerální vlna 100 mm mezi krokvemi + 120 mm volně | 0,22 | ne |
| STR1 plochá část | strop Porotherm Miako 190 + EPS 100 S 100 mm + beton | 0,34 | ne |
| PDL1 podlaha na terénu | — | 0,38 | ne |
| PDL3 strop k nevytápěnému prostoru | — | 0,33 | ne |

Stávající obvodová stěna (Porotherm 40 bez zateplení) vychází ze stejné skladby na U ≈ 0,42 W/m²K.
Slabé místo jsou **stěny S03/S04 k nevytápěné půdě (U 1,3–1,7)** — jejich zateplení by mohlo dát
rezervu k hraničnímu splnění (z úvěru 2 000 Kč/m²); plochu Fáze 0 neuvádí.

## Venkovní stínění — na která okna

Dům nemá klimatizaci, takže stínění **nešetří energii**; platí se za letní komfort (hlavně podkroví).
Plochy podle světových stran (z pohledů v projektu, přepočteno na 49,4 m²):

| Strana | Okna | Přehřívání | Doporučení |
|--------|-----:|------------|------------|
| Západ (hlavní prosklená fasáda) | ≈ 21,5 m² | vysoké — nízké odpolední slunce | **ano** |
| Východ (podkroví) | ≈ 4,1 m² | střední — ranní slunce do ložnic | **ano** |
| Jih | ≈ 11,4 m² | nižší — okna podkroví stíní přesah střechy | volitelně |
| Sever | ≈ 12,4 m² | žádné | ne |

Orientační cena (žaluzie Z-90 s motorem, box do zateplení, montáž) **≈ 6 500 Kč/m²**, z úvěru jen
3 000 Kč/m². Západ + východ (≈ 25,6 m²) ≈ 175 tis. Kč, z toho ≈ 77 tis. z úvěru; všechna okna
≈ 337 tis. Kč, z úvěru 148 tis. Stínění je výhodné dělat **spolu s fasádou** (box v izolantu).

## Rozhodnutí
- [x] ~~Okna ano / ne~~ — **ano**, bez nich KOMPLEX nevyjde (Fáze 0, 15. 10. 2026)
- [ ] Venkovní stínění: žádné / západ + východ (doporučeno) / všechna okna
- [ ] Bílý EPS 200 mm, nebo šedý EPS (~160 mm) — změnu nechat přepočítat Consultorou
- [ ] Zateplit i stěny k nevytápěné půdě (rezerva k hraničnímu splnění)?

## Otázky na Consultoru k Fázi 0
- Kolik rezervy by dalo zateplení stěn S03/S04, 220 mm izolantu nebo okna Uw 0,8?
- Platí 1 830 750, nebo 1 827 250 Kč?
- S01 počítá Porotherm 450 mm, S02 400 mm — překlep?
- Stačí stínění uvést jen na část oken?
- Vyhověl by šedý EPS λ 0,031 v tloušťce 160 mm?
