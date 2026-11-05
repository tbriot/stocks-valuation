# FTNT — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to FTNT (Fortinet).

## Ratio and metric

Price / Adjusted Free Cash Flow (Adj. FCF), TTM. Used since the first note of 19/08/2025 (see `valuations/archive.md`). The first note, of 29/05/2025, used the P/E.

Adj. FCF is a figure published by Fortinet (earnings release, "Reconciliation of net cash provided by operating activities to adjusted free cash flow", and the Supplemental Financials). It is not my computation:

- net cash provided by operating activities
- less purchases of property and equipment
- less proceeds from escrow settlement (one-off, since Q3 2026)
- = free cash flow
- add real estate related purchases (data centers and buildings)
- = adjusted free cash flow

Why Adj. FCF and not FCF: Fortinet invests in its own buildings and data centers. These real estate purchases depress the reported FCF without being recurring operating capex. Q3 2026: FCF $864.8M, Adj. FCF $912.2M (real estate $47.4M). Over the TTM the gap is larger (Q3 2025: $78.4M in the quarter). The risk is that "real estate related" becomes a permanent cost excluded from the base: check in each quarter how much is added back and whether it keeps recurring. Show the plain FCF next to the Adj. FCF in section 1 of the quarterly file.

TTM Adj. FCF is the sum of the last four quarters (each quarter is in the release of the quarter, the prior-year column gives the year before). Checked on the 2026 releases: Q2 2025 427.9 + Q3 2025 645.9 + Q4 2025 588.7 + Q1 2026 1 065.0 = 2 727.5 ($M), which matches the 2 727 of the 06/05/2026 note. The Q4 release gives 2 501.5 for the full year 2025, which matches the 2 501 of the 07/02/2026 note. Q3 2025 TTM computed this way is 2 371.3, against 2 398 in the 06/11/2025 note (taken from the Supplemental Financials): the 27 difference (1%) is negligible and is not investigated (decision of 2026-11-05).

Assumptions after Q3 2026 (pessimistic / neutral / optimistic), given on the published Adj. FCF TTM, not normalized (decision of 2026-11-05): 5-year growth 5% / 12% / 15%, end P/Adj. FCF 18 / 23 / 28. They are my own judgment. The growth combines revenue growth (10% / 12% / 14% a year) and the Adj. FCF margin in year 5 (36% / 45% / 48%, against 45.2% on the TTM and 36.8% in 2025): growth = (1 + revenue growth) x (end margin / 45.2%)^(1/5) - 1, rounded to the unit. The archive records the neutral growth of 14% and the end multiple of 25 (thesis of 19/08/2025), and says that the notes of 2026 stay "very conservative" with 14%, aligned on the optimistic scenario; the other earlier values were not written down. Fair price history: $85 (08/2025), $85 (11/2025), $90 (02/2026), $100 (05/2026), $115 (Q3 2026).

Base not normalized: the TTM Adj. FCF is about 8 points of margin above 2025, partly because deferred revenue grows faster than revenue (billings +29% against revenue +20%; change in deferred revenue is 16.3% of TTM revenue against 11.1% in 2025, 9.7% in 2024, 20.6% in 2023). The two normalizations I looked at (-196 or -419 $M) are estimates; I chose to keep the published figure and lower growth and multiples instead. Check each quarter the share of operating cash flow coming from deferred revenue, accounts payable and inventory.

Buybacks are part of the thesis (see below): the metric is the total Adj. FCF, not per share, so a falling share count is a bonus on top of the growth assumption and must be tracked through the year-over-year change in shares.

## Where to find the data

Files are downloaded with the `fortinet-quarterly-results` skill, as HTML, into `documents/earnings/<year> Q<n>/`: `FTNT-<year>-Q<n>-10-Q.htm` (10-K for Q4) and `FTNT-<year>-Q<n>-Press-Release.htm`. Convert them to text in `/tmp` before reading.

Press release:
- "Reconciliation of net cash provided by operating activities to adjusted free cash flow": FCF, Adj. FCF and margins for the quarter and the prior-year quarter. The Q4 release also gives the full year.
- Revenue, billings (with the change in deferred revenue), non-GAAP operating margin, buyback in the quarter, guidance for the year.
- Balance sheet: cash and investments, debt.

10-Q / 10-K:
- Cash flow statement (year to date): SBC, purchases of property and equipment, repurchases of common stock.
- Debt note (senior notes) and the stockholders' equity note: share repurchases and remaining authorization.
- Legal proceedings and risk factors.

Not scriptable (the IR site blocks scripts), to be downloaded by hand from https://investor.fortinet.com/quarterly-earnings/ into the same folder: Earnings Presentation, Prepared Remarks, Supplemental Financials (Adj. FCF history, billings, RPO, guidance detail).

## Stock-specific points to watch

- **Revenue, billings and guidance:** revenue growth was +14% in 2025 (+12% in 2024), +20% in Q1 2026 and +20% in Q3 2026; billings +31% in Q1 2026 and +29% in Q3 2026 (2 336.3 against 1 807.7). Guidance for 2026 was raised three times (+20% revenue in the Q3 2026 release). February 2026 guidance: +12% a year for the next 3-5 years, which the archive judges conservative. Billings lead revenue: check that the acceleration is not a pull-forward (firewall refresh cycle).
- **Adj. FCF margin:** 58% in Q1 2026 (54.5% in Q1 2025), 43.9% in Q3 2026 (37.4% in Q3 2025). It swings with the timing of billings and working capital, so look at the TTM margin and not the quarter.
- **Real estate add-back:** see the metric section.
- **Buybacks:** irregular and used as a valuation signal by management: $1.83B in Q3 2025 (cash taken from reserves), $57M in Q4 2025, $823M in Q1 2026; authorization increased by $1.2B in Q3 2026 (remaining $2B). Management buys more when the price falls, which supports the pessimistic scenario. Use the share count of the latest filing and the year-over-year change.
- **SBC:** about 10-14% of operating cash flow in the archive, rising 8-10% a year. Not subtracted from Adj. FCF (as for MA, no adjustment), so dilution is tracked by the share count and by the risk indicators table.
- **Operating margin:** non-GAAP operating margin about 35-37%. Sales hiring lowered it in 2025.
- **Multiple risk:** P/E was 46 in May 2025 against a 5-year range of 35-97 (average 55); P/Adj. FCF was 25 in August 2025 and 23 in November 2025. The end multiples of 20 / 25 / 32 are well below the P/E history.
- **Debt and cash:** not yet checked (to do in the first quarterly file, in the risk indicators table). The archive says cash is the buffer for the buybacks (about $2.5B in February 2026).
