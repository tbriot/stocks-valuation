# CSU — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to CSU (Constellation Software, TSX: CSU).

## Ratio and metric

Price / Operating Cash Flow (OCF), TTM, in CAD. The OCF is "Net cash flows from operating activities" in the IFRS statements of CSU (USD). The ratio was changed from P/FCF (note of 08/02/2026) to P/OCF in the note of 14/05/2026: the FCFA2S published by CSU includes one-off items (IRGA / TSS membership liability revaluation, non-cash; interest and dividends received), and capex is very low (TTM capex $77M, 3% of OCF at Q2 2026), so OCF is close to FCF without the noise.

Currency: the shares trade in CAD on the TSX and CSU reports in USD. Everything in the quarterly note is in CAD: TTM OCF in USD x current USD/CAD rate (Yahoo, `USDCAD=X`, rounded to two decimals: an estimate). The prior-quarter fair price is compared with the new one on the same basis, and the decomposition (section 5) separates the OCF effect from the exchange rate effect. The exchange rate used in the May 2026 note is not recorded; it is implied by the figures (CAD 3.85B for USD 2.8B, about 1.375).

TTM OCF is the sum of the last four quarters. The Q4 file (annual statements) gives the full year, so: TTM = full year + year to date - year to date of the prior year. Checked at Q2 2026: 2 732 + 1 374 - 1 260 = 2 846 ($M USD). At Q1 2026: 2 732 + 897 - 827 = 2 802, which matches the USD 2.8B of the 14/05/2026 note.

Shares: 21 191 530 since the IPO in 2007 (no dilution, no buyback, almost no stock-based compensation according to the note of 08/02/2026; not re-checked in the Q2 2026 statements). Use the share count of the statements (identical to Yahoo at Q2 2026).

Assumptions after Q2 2026 (pessimistic / neutral / optimistic): 5-year OCF growth 3% / 7% / 14%, end P/OCF 12 / 18 / 24. They are my own judgment. Before, at Q1 2026: 5% / 7% / 11% and 12 / 18 / 24 (the earlier ones were not written down). The neutral growth (7%) is under the recent pace (OCF +9% over 6 months 2026, +24% in 2025, about +17% a year from 2020 to 2024); the extreme scenarios were widened on 2026-11-06 to bracket the history. At the Q2 2026 price the market implies about 12% growth with an end multiple of 18, or an end multiple of about 23 with 7% growth, for an 11.5% CAGR.

Fair price history (CAD): 2 600 (14/05/2026), 2 750 (Q2 2026). The note of 08/02/2026 has no fair price: it describes a conservative valuation (FCF growth 15%, end multiple 20, against a long-term average of 26).

P/OCF history from my notes (14/05/2026, not refreshed): 10-year min 12.6, median 25.3, max 36.5, 5-year average 27.8; 14.3 at the time, 18.5 at Q2 2026. Public sources define the metric differently: treat them as a rough reference.

Limit of the metric: the consolidated OCF includes 100% of Topicus and Lumine, partly owned by minority shareholders (about 13% of FCFA2S before non-controlling interests in the first half of 2026: 168 of 1 246). P/OCF therefore overstates the cash that accrues to CSU shareholders, which is one reason for end multiples under the historical median. About $1.3B of cash sits in subsidiaries with non-recourse debt and is hard to distribute.

## Where to find the data

Files are downloaded with the `constellation-quarterly-results` skill (PDF) into `documents/earnings/<year> Q<n>/`: `CSU-<year>-Q<n>-MDA.pdf`, `-Financial-Statements.pdf`, `-Shareholder-Report.pdf`. There is no 10-Q (IFRS filings on SEDAR+) and no presentation or guidance. Extract the text to `/tmp` with `pdftotext -layout`.

MD&A:
- "Results of Operations": revenue, expenses, amortization, finance costs, OCF, FCFA2S, weighted shares. Organic growth by revenue type, with and without the exchange rate effect. Altera table.
- "Free cash flow available to shareholders": reconciliation of FCFA2S to OCF (capex, interest, lease payments, non-controlling interests).
- "Liquidity": cash, debt with and without recourse, acquisitions, dividends. "Capital Resources": debt detail.

Financial statements: cash flow statement (three and six months or year), acquisitions note, IRGA liability note.

## Stock-specific points to watch

- **Organic growth:** +3% at Q2 2026 (+1% at constant exchange rates), +6% at Q1 2026 (+1%). Revenue growth (+17% at Q2 2026) comes almost entirely from acquisitions. Recurring revenue +4% (+9% at Q1); Altera at -19%.
- **OCF growth against revenue:** OCF +10% at Q2 2026 and +8.5% at Q1 against revenue +17-20%. Open question from the note of 14/05/2026: how revenue grows 20% with OCF at +9%. If the OCF falls under +7% over one or two quarters, lower the neutral growth.
- **Acquisitions:** a record of USD 1 592M in the first half of 2026 (604 in 2025), more than the OCF. The thesis is that returns on invested capital (ROIC) are good (about 15%, improving with lower software valuations), but the capital deployed weighs less and less against USD 12.6B of TTM revenue. Check the deployed amount each quarter.
- **Debt:** USD 4 196M (Q2 2026), of which 1 472 with recourse to CSI; credit facility undrawn. Net debt / OCF TTM 0.46. Watch the increase and the interest burden (finance costs USD 83M in Q2 2026).
- **IRGA liability:** revalued each quarter against the Topicus share price and the euro; creates large non-cash swings in net income and FCFA2S. Not in the OCF base.
- **Dividend:** small (USD 42M in six months). Buybacks: none, the policy is to invest the FCFA2S in acquisitions above the hurdle rate.
- **Exchange rate:** the TTM OCF in CAD moves with USD/CAD. Record the rate used in each note.
