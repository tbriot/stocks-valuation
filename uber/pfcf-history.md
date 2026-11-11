# UBER — historique du multiple P/FCF

Données: `pfcf-history.csv`. Source: gurufocus (« Uber Technologies Price to Free Cash Flow Ratio Historical Data »), liste fournie par moi le 2026-11-11, recopiée telle quelle. Le multiple est le cours de fin de trimestre divisé par le **FCF par action TTM** (non normalisé: les SBC ne sont pas retirés). La série commence en 2020-03.

Les points de 2020-03 à 2022-03 ont un FCF TTM négatif: la source affiche 0,00, ce qui n'a pas de sens. Je les exclus des statistiques. Les multiples de 2022-06 à 2023-06 (de 51 à 125) viennent d'un FCF presque nul: ils faussent la moyenne et le maximum des fenêtres longues.

## Statistiques calculées sur les fins de trimestre

Calculées par moi à partir de `pfcf-history.csv` (dernier point: 2026-09-30; la ligne du 2026-11-10 est le cours du jour, exclue). À mettre à jour à chaque trimestre.

| Fenêtre | Trimestres | Min | Médiane | Moyenne | Max |
|---|---|---|---|---|---|
| 1 an | 4 | 13,58 | 15,16 | 15,41 | 17,74 |
| 2 ans | 8 | 13,58 | 18,27 | 18,50 | 24,06 |
| 3 ans | 12 | 13,58 | 21,76 | 23,72 | 38,74 |
| Depuis 2022-06 (toute la série valide; 5 ans = même chose) | 18 | 13,58 | 29,80 | 40,87 | 125,22 |

Lecture: pour comparer à un multiple calculé sur le FCF **normalisé** (moins les SBC), multiplier ces valeurs par FCF / FCF normalisé (1,247 au Q3 2026: 10 421 / 8 356).

## Multiple actuel (Q3 2026)

- Source: 13,88 au 2026-11-10 (cours de 70,05 $); fin de trimestre 2026-09-30: 13,58.
- Mon calcul: 13,7 sur le FCF (10 421 M$), 17,1 sur le FCF normalisé (8 356 M$), avec 2 041,9 M d'actions (10-Q).
- Le multiple de fin de trimestre est le **plus bas de la série valide** (13,58 au 2026-09-30). Compression: 24,06 (2025-09), 17,74 (2025-12), 15,47 (2026-03), 14,85 (2026-06), 13,58 (2026-09), alors que le FCF par action a monté de 24 % sur l'année (4,07 $ à 5,05 $).
- Mes multiples finaux sur le FCF normalisé, convertis en FCF simple (division par 1,247): 16 / 22 / 28 correspondent à 12,8 / 17,6 / 22,5 (pessimiste sous le minimum de la série, neutre proche de la médiane sur 2 ans de 18,27, optimiste proche du maximum sur 2 ans de 24,06); 15 / 20 / 26 correspondent à 12,0 / 16,0 / 20,9.
