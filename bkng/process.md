# BKNG — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to BKNG (Booking Holdings, Nasdaq).

## Ratio and metric

Price / Free Cash Flow (FCF), TTM. Chosen on 2026-11-07.

FCF is a figure published by Booking (press release, "Reconciliation of net cash provided by operating activities to free cash flow"), not my computation:

- net cash provided by operating activities
- less additions to property and equipment

Capex is very small. Normalization (decision of 2026-11-07): stock-based compensation is subtracted. The base metric is the normalized FCF = published FCF - SBC (SBC from the cash flow statement; my computation, say so in the quarterly file). No other adjustment so far; working capital swings (deferred merchant bookings) and the FTC settlement are flagged in the quarterly file and decided with me case by case. TTM = last 10-K year - prior year to date + current year to date (Q3 2026 release: nine-month FCF $7 820M against $7 670M).

History of the method (see `valuations/archives.md`): the notes of 2025 used P/E, then a net income estimate; since 22/02/2026 (Q4 2025 results) the valuation is based on FCF.

Assumptions at Q1 2026 (pessimistic / neutral / optimistic), my own judgment: 5-year FCF growth 9% / 11% / 16%, end P/FCF 14 / 17 / 28. Fair price at the time: about $195 (after the 25:1 split; $204 before the update). The 10-year median multiple was noted as around 20 in February 2026.

Assumptions after Q3 2026 (pessimistic / neutral / optimistic), on the normalized FCF (FCF - SBC), my own judgment: 5-year growth 6% / 10% / 15%, end P/FCF 13 / 18 / 23. Fair price $195. The multiples are on the normalized FCF: a multiple on the published FCF is multiplied by published FCF / normalized FCF (1.069 at Q3 2026) to compare. The end multiples of Q1 2026 (14 / 17 / 28, on the published FCF) are equivalent to 15.0 / 18.2 / 29.9 on the normalized FCF.

Notes: my past notes are kept in `valuations/archives.md` (decision of 2026-11-07: keep this name, and do not use the `<year>-archive.md` format for BKNG).

Share price: the 25:1 stock split makes older prices in the notes pre-split unless stated; the archive of 28/04/2026 is already adjusted.

## Where to find the data

Documents are downloaded by the `booking-quarterly-results` skill into `documents/earnings/<year> Q<n>/`, as PDFs: `BKNG-<year>-Q<n>-Press-Release.pdf`, `-10-Q.pdf` (`-10-K.pdf` for Q4), `-Presentation.pdf`, `-Prepared-Remarks.pdf`, `-Transcript.pdf`.

To be completed after the first read of the filings (statement pages, notes on debt, buybacks and share count, segment data).

## Stock-specific points to watch

To be completed with me (for example room nights, gross bookings, take rate, buybacks, debt, regulation).

## Reference data kept in the folder

- `pfcf-history.csv` and `pfcf-history.md`: history of the P/FCF multiple (gurufocus, quarter ends since 2006-12, provided by me on 2026-11-07) and precomputed min, median, mean and max over 1, 2, 3, 5, 10 years and the full series. The multiple is on the published FCF per share (SBC not subtracted): multiply by published FCF / normalized FCF to compare with the normalized multiple. Update both files each quarter with the new data point (and the statistics).
- `buybacks.csv`: share repurchases per quarter (total from the statement of stockholders' equity of the 10-Q/10-K, including shares withheld for taxes; the press release figure is lower), shares repurchased, and the amount as % of the quarter-end market cap and of the shares at the start of the quarter. Add a row each quarter (decision of 2026-11-07: buybacks are followed closely because a good part of the FCF per share growth depends on them). Market cap at quarter end = quarter-end price x shares outstanding.
- Company long-term ambition (no horizon given, constant currency, "at least"): 8% growth in gross bookings and adjusted revenue, 15% in adjusted EPS (per share, buybacks included).
