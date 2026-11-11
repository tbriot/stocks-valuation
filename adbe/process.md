# ADBE — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to ADBE (Adobe Inc., Nasdaq).

## Ratio and metric

Price / Free Cash Flow (FCF), TTM (the ratio used in my notes of September 2025, see `valuations/archives.md`).

Adobe does not publish a free cash flow figure in the press release or the 10-Q: FCF is my computation from the cash flow statement.

- net cash provided by operating activities
- less purchases of property and equipment

Normalization (decision of 2026-11-11): stock-based compensation is subtracted. The base metric is the normalized FCF = FCF - SBC (SBC from the cash flow statement; my computation, say so in the quarterly file). The plain FCF is shown next to it. In September 2025 the multiple was 16,2 on the plain FCF and 20,1 without SBC; SBC is about 19-20 % of operating cash flow.

TTM = last 10-K year - prior year to date + current year to date (Q3 FY2026 10-Q: nine-month operating cash flow $7 646M against $6 871M, purchases of property and equipment $180M against $145M, SBC $1 582M against $1 453M).

Assumptions of September 2025 (pessimistic / neutral / optimistic), my own judgment, on the plain FCF TTM (SBC not subtracted):

- average 5-year FCF TTM growth: 8 % / 10 % / 13 %
- end P/FCF TTM multiple (5 years): 14 / 18 / 25
- fair price at the time: $385

A multiple on the plain FCF is multiplied by plain FCF / normalized FCF to compare with a multiple on the normalized FCF (1,243 at Q3 FY2026): the end multiples of 14 / 18 / 25 are equivalent to 17,4 / 22,4 / 31,1 on the normalized FCF. These assumptions are reviewed at the first quarterly update (Q3 FY2026).

## Where to find the data

Documents are downloaded by the `adobe-quarterly-results` skill into `documents/earnings/<fiscal year> Q<n>/`, as PDFs: `ADBE-<year>-Q<n>-10-Q.pdf` (`-10-K.pdf` for Q4), `-Press-Release.pdf`, `-Script-Slides.pdf`, `-Transcript.pdf` and, from 2026 Q2, `-Investor-Datasheet.pdf`.

Fiscal calendar: the year and quarter in folder names are Adobe's fiscal ones. The fiscal year ends the Friday closest to November 30 (FY2025 ended November 28, 2025). Q3 FY2026 ended August 28, 2026. Results are published about 2-3 weeks after quarter end.

To be completed after the first read of the filings (statement pages, notes on debt, buybacks and share count, segment data).

## Stock-specific points to watch

From my notes of September 2025 (to be confirmed and completed with me):

- Stock-based compensation (about 20 % of operating cash flow) and its growth against revenue.
- Buybacks: Adobe buys back about 2 % of the shares per year, more when the price falls; the share count fell by 5,4 % over the TTM at the time. Cash is taken from reserves to buy more.
- Debt (almost none) and cash.
- FCF margin (41 % TTM) and ROCE (48 % TTM).
- Disruption risk from AI and competition (Figma, Canva); subscription price increases; switching costs of the products; AI features included in the products; growth of the addressable market.

## Reference data kept in the folder

- `pfcf-history.csv` and `pfcf-history.md`: history of the P/FCF multiple (gurufocus, quarter ends since 2006-11, provided by me on 2026-11-11) and precomputed min, median, mean and max over 1, 2, 3, 5, 10 years and the full series. The multiple is on the FCF per share with SBC not subtracted: multiply by FCF / normalized FCF to compare with the normalized multiple. Update both files each quarter with the new data point (and the statistics).
