---
title: Úspory a návratnost
parent: Model úspor
nav_order: 2
---

# Úspory a návratnost

> **Orientační výpočet 14. 10. 2026** — nezávislý podklad ke srovnání s Fází 0 (Consultora).
> Interaktivní verze s posuvníky (ceny energií, ceny opatření, FVE, splatnost, U hodnot):
> **[Model úspor — artefakt](https://claude.ai/artifact/EREti4jdXNLE9oRaVWiofE)** (soukromý odkaz).
>
> **Použité předpoklady:** [Předpoklady modelu](predpoklady.html) + níže. Ceny energií 2026 (mezní),
> plochy z projektové dokumentace ([Parametry domu](../02-dum/parametry-domu.html#plochy-z-vykresu)),
> tržní ceny 2026, úvěr bezúročný na **15 let**. Spotřeba plynu = **průměr 2021/22–2025/26: 38 072 kWh/rok**,
> ceny energií = ceník innogy Optimal 36 pro rok 2026 (vč. stálých plateb).

## Varianty (1. rok, dnešní ceny)

| | Dnes | **A** — fasáda + střecha + FVE | **B** — A + okna a dveře |
|---|---:|---:|---:|
| Spotřeba plynu (kWh/rok) | 38 072 | ≈ 29 470 (−8 600) | ≈ 23 170 (−14 900) |
| Plyn (Kč/měs.) | 5 454 | 4 349 (−1 105) | 3 541 (−1 913) |
| Elektřina (Kč/měs.) | 3 328 | 1 303 | 1 303 |
| **Energie celkem (Kč/měs.)** | **8 782** | **5 652** | **4 844** |
| Splátka úvěru (Kč/měs.) | — | 5 956 | 8 930 |
| **Celkem během splácení (Kč/měs.)** | **8 782** | **11 607** (+2 825) | **13 774** (+4 992) |
| **Po splacení (16. rok, dnešní ceny / +2 % ročně)** | 8 782 / 11 820 | 5 652 / 7 804 | 4 844 / 6 717 |
| Úspora energie (Kč/rok) | — | ≈ 37 600 | ≈ 47 300 |
| Úspora plynu na vytápění | — | 25 % | 43 % |
| Úspora dodané energie (vytápění + TV) | — | ≈ 23 % ⚠ pod 30 % | ≈ 39 % ✓ |
| Investice (Kč) | — | ≈ 1 179 000 | ≈ 1 741 000 |
| Úvěr (Kč) = způsobilé výdaje | — | ≈ 1 072 000 | ≈ 1 607 000 |
| Vlastní zdroje (Kč) | — | ≈ 107 000 | ≈ 134 000 |
| Návratnost investice (růst cen 2 %/rok) | — | ~26 let | ~29 let |

_Model dnes vychází na ≈ 105 tis. Kč/rok energií (skutečnost 2025/26 ≈ 107 tis.); rozdíl jsou ceny elektřiny
z 2. pol. 2025 (dražší silová elektřina a poplatek za OZE)._

## Po opatřeních

| Opatření | Investice (Kč) | Max. z úvěru (Kč) | Úspora (kWh/rok) | Úspora (Kč/rok) | Prostá návratnost (roky) | Poznámka |
|----------|---------------:|------------------:|-----------------:|----------------:|-------------------------:|----------|
| Zateplení fasády (230 m², šedý EPS 160 mm, 2 400 Kč/m² na klíč) | 552 000 | 552 000 (strop 805 000) | } 8 600 plynu | } 13 250 | } ~48 | U stěn 0,35 → 0,13; zakryje tepelné mosty (I-profily nad okny) |
| Oprava izolace střechy | 80 000 | 80 000 | (v řádku výše) | | | rozsah nejistý (kuny) |
| Okna 44,69 m² + dveře 12,11 m² (9 000 / 11 000 Kč/m²) | 535 000 | 535 000 (strop 682 000) | 6 300 plynu | 9 700 | **~58** | Uw 1,5 → 0,85, menší infiltrace |
| FVE 8 kWp + baterie 10 kWh | 356 000 | } 350 000 (strop C.3) | výroba 8 000; vlastní spotřeba 3 600, přetoky 4 400 | 24 300 | ~16 | ekonomicky nejsilnější |
| Wallbox | 30 000 | (v limitu FVE) | — | — | — | bez EV nic nešetří |
| Služby Consultora | 110 000 | 90 000 | — | — | — | Fáze 3+4 (20 000) z vlastních |
| Rezerva 5 % | 51 000 / 78 000 | 0 | — | — | — | z vlastních |

## Citlivost

| Co se změní | Dopad |
|-------------|-------|
| U stávajících stěn 0,60 místo 0,35 | úspora vytápění ve variantě A ≈ 33 % místo 25 %; A by se dostala k hranici 30 % |
| Těsnost dnes horší (výměna vzduchu 0,8 h⁻¹) | větší přínos výměny oken i fasády |
| Ceny energií +/− 20 % | úspora energie ±7–9 tis. Kč/rok |
| Výroba FVE −10 % | úspora −2,4 tis. Kč/rok |
| Výkup přetoků 0 Kč/kWh | úspora −3,5 tis. Kč/rok |

## Závěr

- **Úvěr 2 mil. Kč při těchto cenách nevyjde** — úvěr nesmí převýšit faktury za způsobilá opatření;
  ve variantě A je strop ≈ 1,07 mil., v B ≈ 1,6 mil. Kč.
- **Během splácení zaplatíme měsíčně víc než dnes** (A +2,8 tis., B +5,0 tis. Kč/měs.); po splacení
  (15 let) ušetříme ≈ 3,1 tis. (A) / 3,9 tis. (B) Kč/měs. v dnešních cenách Za 30 let vyjde B i A levněji než dnešní stav.
- **Okna se samy nezaplatí** (návratnost ~58 let), ale model naznačuje, že **bez nich nemusí projít
  podmínka 30 % úspory dodané energie** pro komplexní renovaci — stěny už dnes nejsou špatné (Porotherm/Hebel 400 mm).
  FVE se podle metodiky PENB v plynem vytápěném domě započte jen omezeně (odhad, ověřit ve Fázi 0).
- **Rozhodne Fáze 0** — porovnat hlavně U stávajících konstrukcí, % úspory ve variantě bez oken a výši úvěru.

## Nejistoty

Úspora vytápění ±30 % (U hodnoty a těsnost jsou odhad, model kalibrovaný na skutečnou spotřebu
vysvětluje ~90 % plynu na topení), ceny prací ±20 %, výkup přetoků a vývoj cen energií po 11/2027.
Výměna baterie FVE (za 12–15 let) a elektromobil v modelu nejsou.
