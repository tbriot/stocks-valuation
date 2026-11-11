---
name: expected-cagr
description: Expected 5-year CAGR of a stock at the current share price, using the latest assumptions (growth, end multiple, fair price) of this repository. Takes a ticker symbol (AMZN, GOOG, MA, CSU, FTNT, ADBE, BKNG) and returns a table with the three scenarios and the gap between the current price and the fair price. Takes "all" (or no ticker) and returns one ranking table of every stock of the repository, sorted by neutral CAGR. Use when the user asks what return or CAGR to expect from a stock at today's price, to compare or rank the stocks, or whether one is over- or undervalued against the fair price.
---

# Expected CAGR at the current price

Input: a ticker symbol, or `all` (also when no ticker is given and the user asks for all stocks). Output: the table below (one ticker) or the ranking table (all), from the assumptions of the latest quarter in `<ticker>/history.csv`.

## Run

1. Get the current price(s) with the `stock-quote` skill (fallback: web search). For CSU, which the repository tracks in CAD, quote `CSU.TO`. For `all`, quote every ticker that has a `<ticker>/history.csv` in one call.
2. Pass it to the script:

```
python3 .claude/skills/expected-cagr/scripts/expected_cagr.py FTNT --price 123.57 --price-date 2026-11-10 --source "Yahoo Finance via yfinance"
```

For all stocks (one `--price TICKER=value` per ticker found in `*/history.csv`; the script lists the missing ones if any):

```
python3 .claude/skills/expected-cagr/scripts/expected_cagr.py all --price AMZN=270.87 --price FTNT=123.57 ... --price-date 2026-11-10 --source "Yahoo Finance via yfinance"
```

The output is a JSON list already sorted by neutral CAGR at the current price, descending.

The script does not fetch any price. It reads the rows of the latest quarter of `<ticker>/history.csv` (growth, end multiple, end market cap, shares, fair price) and prints JSON.

Computation: price in year 5 = end market cap / shares; CAGR = (price in year 5 / price)^(1/5) - 1, at the current price and at the fair price. Gap = current price / fair price - 1 (negative: discount, positive: premium), as in Step 4 of `valuation-process.md`.

## Answer format, one ticker (in French, number format of CLAUDE.md: space for thousands, comma for decimals)

1. One line: the current price with its source and date, no request to confirm it (the price is cited, not confirmed), the fair price and the quarter of the assumptions.
2. The gap with the fair price, **in bold and on its own line**, with the sign and the word "décote" or "prime", for example: `Écart avec le prix juste: **+7,5 %** (prime): 123,57 $ contre 115 $.`
3. The table:

| | Pessimiste | Neutre | Optimiste |
|---|---|---|---|
| Croissance 5 ans | | | |
| Multiple final (<metric>) | | | |
| Prix par action en année 5 | | | |
| **CAGR au prix courant** | | | |
| CAGR au prix juste | | | |

4. One or two sentences: how the neutral CAGR compares with the 11-12 % target and the pessimistic CAGR with the -2 to -3 % limit (Step 4 of `valuation-process.md`). Mention the quarter of the assumptions: if a newer earnings release is out, say that the assumptions are not yet updated.

## Answer format, all stocks (in French)

1. One line: the source and date of the prices (several dates if they differ), no request to confirm them.
2. One table, rows in the order of the script output (neutral CAGR at the current price, descending). Columns: ticker, price (with currency: USD, and CAD for CSU), fair price, gap with the fair price (bold, signed, "décote" or "prime"), then the CAGR at the current price for the pessimistic, neutral (bold) and optimistic scenarios, and the quarter of the assumptions:

| Titre | Prix courant | Prix juste | Écart | Pessimiste | **Neutre** | Optimiste | Hypothèses |
|---|---|---|---|---|---|---|---|

3. One or two sentences: which stocks meet the neutral target (11-12 %) and the pessimistic limit (-2 to -3 %), and any stock whose assumptions are older than its latest earnings release. CAD and USD figures are percentages, so the ranking is comparable across currencies.

## Rules

- Do not recompute the assumptions or propose new ones: they are my own judgment, stored in the CSV. If the user wants other hypotheses, compute them separately and say so.
- Do not write holdings, share counts of positions or cost basis anywhere.
- The ticker has no `history.csv` (no valuation yet): say so, do not guess.
