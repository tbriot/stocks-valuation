# UBER — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to UBER (Uber Technologies, Inc., NYSE).

## Ratio and metric

Price / Free Cash Flow (FCF), TTM (the ratio used in my notes since May 2025, see `valuations/archives.md`).

Uber publishes a free cash flow figure (press release, reconciliation table at the end): net cash provided by operating activities less purchases of property and equipment. Capex is very low, so this FCF is close to the operating cash flow, not a "real" free cash flow: the end multiples are lower than they would be for a company with heavy capex.

Normalization: stock-based compensation is subtracted (my notes since June 2025). The base metric is the normalized FCF = FCF - SBC (SBC from the cash flow statement; my computation, say so in the quarterly file). The plain FCF is shown next to it. SBC is about 20 % of operating cash flow.

TTM = last fiscal year (Q4 press release) - prior year to date + current year to date (nine-month figures in the Q3 press release; the press release has no 10-Q behind it here, see below).

Assumptions after Q3 2026 (pessimistic / neutral / optimistic), my own judgment, on the FCF TTM minus SBC (decision of 2026-11-11; the multiples are on the same metric):

- average 5-year growth of the FCF TTM minus SBC: 12 % / 16 % / 25 % (13 % / 18 % / 25 % after Q1 2026)
- end P/FCF TTM multiple (5 years): 15 / 18 / 25 (16 / 22 / 28 after Q1 2026)
- fair price: $90 (was $110 in May 2026)

The growth and multiples are on organic figures: Delivery Hero (offer of July 2026, closing expected in the second half of 2027) is not included. The UK VAT payment of about $1,5B expected in Q4 2026 is not normalized: show the Q4 TTM with and without it.

## Where to find the data

The fiscal year is the calendar year. Results come about 5 weeks after quarter end (Q3 in early November).

The press release holds the statements of operations, balance sheet and cash flows (quarter and year to date, with the prior-year comparison), the free cash flow reconciliation, the weighted-average share counts and the segment data (Mobility, Delivery, Freight). The 10-Q/10-K is not downloaded: it is only needed for the shares outstanding at the cover date, the debt detail (maturities, rates), litigation and the equity investments.

To be completed after the first quarterly update (statement pages, buybacks and share count).

Documents go into `documents/earnings/<year> Q<n>/` (git-ignored), downloaded by the `uber-quarterly-results` skill: `UBER-<year>-Q<n>-Press-Release.pdf`, `-Supplemental-Data.pdf`, `-Prepared-Remarks.pdf`, `-Transcript.pdf`. No 10-Q/10-K yet.

## Stock-specific points to watch

From my notes of May 2025 to May 2026 (to be confirmed and completed with me):

- FCF and OCF growth against the revenue / gross bookings growth (about +20 %): I expect FCF growth above 20 %, closer to 30 %.
- Stock-based compensation (about 20 % of operating cash flow) and its growth against the cash flow.
- Operating margin by segment: Mobility (7,7 % at Q1 2026) and Delivery (3,7 %). Can Delivery converge towards Mobility? Operating leverage on Mobility, whose margin is still low.
- Guidance against actual results (the guidance has been conservative so far).
- Durability of the competitive advantage (moat): doubtful in the long term, hence the need for a margin of safety.
- Non-GAAP EPS is hard to interpret (adjustments, revaluation of equity investments in GAAP net income).

## Reference data kept in the folder

- `pfcf-history.csv` and `pfcf-history.md`: history of the P/FCF multiple (gurufocus, quarter ends since 2020-03, provided by me on 2026-11-11) and precomputed min, median, mean and max over 1, 2, 3 years and the valid series (positive FCF only, from 2022-06). The multiple is on the FCF per share with SBC not subtracted: multiply by FCF / normalized FCF to compare with the normalized multiple. Update both files each quarter with the new data point (and the statistics).
- `history.csv` and `risk-indicators.csv` contain only the header for now (same columns as `adbe/`).
