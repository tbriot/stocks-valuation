# BKNG — historique du multiple P/FCF

Données: `pfcf-history.csv`. Source: gurufocus (« Booking Holdings Price to Free Cash Flow Ratio Historical Data »), liste fournie par moi le 2026-11-07, recopiée telle quelle. Le multiple est le cours de fin de trimestre divisé par le **FCF par action TTM publié** (non normalisé: les SBC ne sont pas retirés). Les prix sont ceux de la source (ajustés du split 25:1).

## Références de la source (au 2026-11-07)

- P/FCF actuel: 13,59, soit 31 % sous sa médiane sur 10 ans.
- Sur 10 ans (valeurs quotidiennes, pas seulement les fins de trimestre): minimum 11,26, médiane 19,58, maximum 99,7.

## Statistiques calculées sur les fins de trimestre

Calculées par moi à partir de `pfcf-history.csv` (dernier point: 2026-09-30; la ligne du 2026-11-06 est exclue). Les deux trimestres à FCF négatif (2020-12 et 2021-03, la source affiche 0,00) sont exclus des statistiques: « Valeurs » donne le nombre de points retenus. À mettre à jour à chaque trimestre.

| Fenêtre | Trimestres | Valeurs | Min | Médiane | Moyenne | Max |
|---|---|---|---|---|---|---|
| 1 an | 4 | 4 | 13,46 | 14,77 | 15,52 | 19,10 |
| 2 ans | 8 | 8 | 13,46 | 18,54 | 17,84 | 21,13 |
| 3 ans | 12 | 12 | 13,46 | 18,05 | 17,85 | 21,13 |
| 5 ans | 20 | 20 | 11,89 | 17,41 | 17,86 | 38,53 |
| 10 ans | 40 | 38 | 11,89 | 18,46 | 22,72 | 85,27 |
| Depuis 2006-12 (toute la série) | 80 | 78 | 11,25 | 20,18 | 22,67 | 85,27 |
| Depuis 2022-03 (hors COVID) | 19 | 19 | 11,89 | 16,85 | 16,77 | 21,60 |

Lecture: pour comparer à un multiple calculé sur le FCF **normalisé** (moins les SBC), multiplier ces valeurs par FCF publié / FCF normalisé (1,069 au Q3 2026: 9 237 / 8 643). Le multiple de fin de trimestre est parfois très différent du multiple quotidien: la médiane sur 10 ans de la source (19,58) diffère de celle calculée ici (18,46) pour cette raison.

## Multiple actuel (Q3 2026)

- Source: 13,59 (2026-11-07); fin de trimestre 2026-09-30: 13,46.
- Mon calcul: 12,9 sur le FCF publié (9 237 M$), 13,8 sur le FCF normalisé (8 643 M$), cours de 160,67 $ (2026-11-06) et 743,701 M d'actions.
