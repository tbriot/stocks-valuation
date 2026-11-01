# Stock valuation process

Quarterly exercise, run for every stock in my portfolio and for some stocks on my watchlist. It is a simple 5-year scenario valuation done in a Google Sheet. This file holds the rules that apply to all stocks. What is specific to one stock (metric definition, adjustments, data sources) lives in `<ticker>/process.md`. Quarterly notes live in `<ticker>/valuations/` and source documents in `<ticker>/documents/`. The same layout is used for every stock.

## Principle

Pick one valuation ratio that fits the company. Assume how the underlying metric grows over 5 years and what multiple the market will put on it at the end. That gives a target market cap in year 5 and a CAGR from today's price. Repeat for three scenarios (pessimistic, neutral, optimistic). Then set a fair price that leaves a margin of safety.

## Step 1: Choose the metric and ratio

Choose the ratio that is most relevant for the stock, for example P/OCF, P/E or P/FCF. The metric is always TTM, so it is refreshed every quarter. The metric definition, and any adjustment to it, is written in `<ticker>/process.md`.

## Step 2: Current valuation (sheet section "With current price")

| Input | Notes |
|---|---|
| Exchange, ticker | |
| Current share price | Get it with the `stock-quote` skill (Yahoo Finance via yfinance, unofficial). Give the source and the date, and I confirm it before it is used. If the skill fails, fall back to a web search |
| Current market cap, or current shares count | Enter one; the other is derived (market cap = price x shares). Prefer the share count from the latest filing over the one from `stock-quote`, and say which one is used |
| Current metric (TTM) | In millions |
| Current ratio | market cap / metric |

## Step 3: Scenarios (sheet section "With current price")

For each of pessimistic, neutral and optimistic, I enter two assumptions by hand:

- **5y average growth** of the metric
- **End ratio**, the multiple at year 5

The sheet computes:

- end metric = current metric x (1 + growth)^5
- end market cap = end metric x end ratio
- CAGR = (end market cap / current market cap)^(1/5) - 1

The growth rates and multiples are my own judgment. They are not computed or taken from consensus. Any proposal for new values is a suggestion until I confirm it.

## Step 4: Fair price (sheet section "Finding a fair price")

- **My fair share price** is a judgment call, not a formula output.
- Fair market cap = fair price x shares.
- The CAGRs are recomputed from the fair price.

Targets for the fair price:

- the neutral CAGR is about 11-12% a year (target expected return)
- the pessimistic CAGR loses no more than 2-3% a year (margin of safety)

How to find it:

1. Compute the three CAGRs for a range of prices, in steps of $5.
2. Pick the price that meets both targets.
3. If both cannot be met at the same time, pick the price at the edge of both, say which target is stretched, and show the nearby prices. I make the final call.
4. Round to a multiple of $5.

Compare the current price with the fair price to see how undervalued or overvalued the stock is.

## Step 5: Quarterly update routine

After each earnings release (10-Q, earnings release, presentation):

1. Read `<ticker>/process.md` for the metric definition and stock-specific adjustments.
2. Update the TTM metric and the current ratio.
3. Compare the current ratio with its history: 10-year median, 5-year average, 3-year average (for example from gurufocus). Public sources may use a different metric definition than the adjusted one, so treat them as a rough reference.
4. Review the quarter against the thesis: metric growth versus the assumed rate, segment growth and margins, capex, cash and debt, and management guidance for the next quarter.
5. Normalize the base metric: stock-based compensation, deferred taxes, working capital, one-offs, as described in `<ticker>/process.md`.
6. Adjust the growth and end multiples with new information. Higher expected growth raises the assumptions. More debt or uncertainty lowers the target multiples. For each change, note whether the information is about the past (already in the base) or about the future (guidance, risk), to avoid counting good news twice.
7. Set the new fair price (Step 4).
8. Write `<ticker>/valuations/<year>-Q<n>.md` with six sections: (1) results analysis; (2) assumption review, with the reason for each change and the risk indicators; (3) one table with the assumptions and the valuation at the current price (one row each for growth and end multiple, with the previous quarter's value in brackets on the same row); (4) the fair price, shown as a large heading (`# 330 $`), then, each as its own paragraph (blank line between), the previous fair price in brackets (`(précédent: 345 $)`) and the current price with its date and the gap with the fair price (`Prix courant: 240,35 $ (2026-10-30) — écart avec le prix juste: **-27,2 %** (décote).`), then a table of end metric, end market cap and CAGR at the fair price. The gap is current price / fair price - 1, with a sign: negative is a discount, positive is a premium. The fair market cap is not shown; (5) the breakdown of the fair price change (base, growth, multiple); (6) external references: valuations by analysts, YouTubers or bloggers I follow, in a table (source, date, fair price or target, assumptions, link). They are for comparison only and do not set my fair price. When I give a link, record it as is (timestamp included) and leave the other fields as "à compléter" until I give the values: do not guess them from the title or from memory.
9. Append three rows (one per scenario) to `<ticker>/history.csv` and one row to `<ticker>/risk-indicators.csv`.

Also save a screenshot of the valuation matrix in `<ticker>/valuations/`, named `<year>-Q<n>-valuation.png`.

## Criteria for the end multiple

The chosen metric (for example OCF) does not capture everything, so the end multiples are also driven by criteria outside it. When one of them worsens, lower the multiples; when it improves, raise them:

- debt level and interest burden (higher debt means lower multiples)
- free cash flow after capex
- dilution from stock-based compensation
- size of the company at year 5

Record which criterion moved the multiples in the "reason" column of the quarterly file.

Each quarterly file has a risk indicators table, and `<ticker>/risk-indicators.csv` keeps one row per quarter:

- long-term debt, as a ratio to TTM operating cash flow and to TTM operating income (net income can be distorted by non-cash gains)
- net debt (long-term debt minus cash and marketable securities) over TTM operating cash flow
- TTM free cash flow
- quarterly interest expense and interest coverage (operating income / interest expense)
- shares outstanding year-over-year change, and TTM stock-based compensation as a share of TTM operating cash flow

## Repository layout

```
CLAUDE.md                           entry point for Claude
valuation-process.md                general rules (this file)
<ticker>/
  process.md                        stock-specific rules and methods
  valuations/
    <year>-Q<n>.md                  one file per earnings release
    <year>-Q<n>-valuation.png       screenshot of the valuation matrix
    <year>-archive.md               older notes
  history.csv                       one row per scenario per quarter
  risk-indicators.csv               one row per quarter
  documents/earnings/<year> Q<n>/   10-Q, earnings release, presentation
```
