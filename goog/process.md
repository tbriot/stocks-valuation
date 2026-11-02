# GOOG — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to GOOG (Alphabet).

## Ratio and metric

Price / adjusted Operating Cash Flow (OCF), TTM.

Adjusted OCF = reported TTM OCF - temporary part of deferred taxes - TTM stock-based compensation (SBC).

Why OCF and not earnings: capex is very high, and net income is distorted by unrealized gains and losses on equity investments (SpaceX, a private company before its IPO) and by the "Other Bets" investments. The Q1 2026 valuation already switched to P/OCF TTM.

Reference multiples (Q1 2026 note, on reported OCF, so only a rough guide for the adjusted metric): 10-year median 18.3, min 12.5, max 27; 3-year average 18.2; 5-year average 18.7.

Assumptions after Q3 2026 (on adjusted OCF, pessimistic / neutral / optimistic): 5-year growth 9% / 14% / 19%, end P/OCF 15 / 18 / 24. Fair price $240. The Q1 2026 assumptions were on reported OCF (growth 11 / 17 / 22%, multiples 14 / 17 / 24, fair price $310), so they are not directly comparable.

Growth of the adjusted OCF in 2024-2025 (+29%, +36%) is not a base rate: about half of the 2025 increase came from a deferred tax swing and working capital. Revenue grew 14-15% a year; the neutral 14% means revenue +13% a year with a stable adjusted OCF margin (about 33%).

## Where to find the data

Earnings release:
- Cash flow statement (page 5 of the Q3 2026 release): OCF, SBC, deferred income taxes, gain/loss on securities, capex. The columns are the quarter and the year to date, so the TTM is: last 10-K year - prior year to date + current year to date.
- Non-GAAP reconciliation table (end of the release): quarterly OCF, capex and FCF, and the TTM figures. Use it to cross-check the TTM OCF.
- Balance sheet: long-term debt, cash and marketable securities.

10-Q:
- Note 14 (income taxes) and the "Provision for income taxes" section of the MD&A: effective tax rate and its drivers. It does not give the deferred tax split.
- "Other income (expense), net" table in the MD&A: gains and losses on equity securities (the SpaceX and private company piece), interest income and interest expense.
- Note on stock-based compensation: unrecognized compensation cost.

Presentation: segment growth and margins (Google Services, Google Cloud), backlog.

## Why adjust the OCF

- **SBC:** a real cost paid in shares, added back by the cash flow statement, so we subtract it. It is significant: Q3 2026 TTM $30.4B, 16.9% of reported OCF, and rising ($8.6B in Q3 2026 alone, against $6.4B a year earlier).
- **Deferred taxes:** same logic as AMZN, see below. Probably smaller than for AMZN.

## Method for the deferred tax adjustment

All figures are TTM, from the cash flow statement unless stated.

1. Take the "Deferred income taxes" line (Q3 2026 TTM: $34.3B; for 2025: $8.3B).
2. Remove the part linked to unrealized gains on equity securities. The cash flow statement removes these gains from OCF ("Loss (gain) on debt and equity securities, net": $126.8B of gains for the first nine months of 2026) and adds back the deferred tax on them. The two cancel out, so this piece is neutral for OCF. Estimate it at the statutory rate (about 21%, plus state taxes) of the TTM gains, since the 10-Q gives no figure.
3. The rest is the real tax deferral.
4. The temporary part is the real deferral minus the level of a year earlier, taken as the normal level. Do not count it if it is negative or near zero. At Q3 2026 the rest was about $7B TTM (about $5.6B at Q1 and $6.2B at Q2), close to the level of a year earlier, so no temporary part is removed.
5. Subtract the temporary part from reported OCF.

This is an estimate. Check at Q3 2026: 21% of the $129.1B TTM gains on securities is about $27.1B, against $34.3B of deferred taxes over the same period. The rest is about $7.2B. So the temporary part looks small, unlike AMZN. State clearly in the quarterly file that this is an estimate.

## Stock-specific points to watch

- **Capex vs OCF:** in Q3 2026 capex ($51.4B) exceeded OCF ($42.3B); TTM FCF is only $19.7B. Debt: long-term debt went from $46.5B (end of 2025) to $125.1B (Q3 2026); interest expense $1.0B in Q3 2026 against $0.1B a year earlier.
- **SpaceX and private holdings:** large non-cash gains and losses in "Other income (expense), net" inflate or depress net income and EPS (do not use them for ratios). Q3 2026 showed $8.7B of losses on equity securities after the SpaceX IPO.
- **Google Cloud:** growth, operating margin and backlog (about $460B at Q1 2026) are the main drivers of the growth assumptions. Its share of revenue keeps rising.
- **Google Search:** check for any slowdown against AI chatbots (none seen up to Q1 2026).
- **Acquisitions:** $34.1B of acquisitions in the first nine months of 2026, to watch for the share count and the cash flow.
- **Dilution and buybacks:** the adjusted OCF already pays for stock-based compensation in cash, so the share count is held constant (no extra dilution, to avoid counting it twice). Only share issues not covered by SBC are added: at Q3 2026, +48M shares for the conversion of the mandatory convertible preferred stock (12,342M shares in total). Buybacks stopped in 2026 (none over nine months, against $39.8B a year earlier) and the share count grew 1.8% year on year; the $40B at-the-market program (June 2026) is meant for taxes on employee equity grants. Watch the year-over-year change in shares: if shares are issued beyond SBC (for example to fund capex), lower the end multiples. Each extra point of net dilution a year costs about 1 point of CAGR.
- **Consistency with AMZN:** compare the two stocks on fair market cap and on fair market cap / adjusted OCF (Q3 2026: GOOG 19.9, AMZN 20.9), not on price per share. The growth assumptions are 1 point lower for GOOG, by choice of prudence and not because of evidence that AMZN grows faster.
