# AMZN — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to AMZN.

## Ratio and metric

Price / adjusted Operating Cash Flow (OCF), TTM.

Adjusted OCF = reported TTM OCF - temporary part of deferred taxes - TTM stock-based compensation (SBC).

The end multiples are calibrated on the adjusted metric. Historical multiples from public sources (for example gurufocus: 10-year min 16, median 26, max 47 on reported OCF) use reported OCF, so they are only a rough reference.

## Where to find the data

Earnings release, "Supplemental Financial Information" tables (pages 11-13): TTM OCF, TTM FCF, shares outstanding, segment results, TTM operating income. Cash flow statement (page 6): deferred income taxes, SBC, interest paid. Balance sheet (page 10): long-term debt, cash, marketable securities. Statement of operations (page 7): interest expense.

The 10-Q has the income tax note (deferred taxes, Anthropic-related tax, cash taxes paid) and the liquidity section.

## Why adjust the OCF

- **SBC:** it is a real cost paid in shares (dilution of about 1.2% a year), but the cash flow statement adds it back. We subtract it.
- **Deferred taxes:** part of the deferred tax add-back is temporary. It comes from tax rules (full expensing of capex, amortization of capitalized R&D, IRS Notice 2026-7) that cut cash taxes while capex is very high. It shrinks if capex stabilizes.

## Method for the deferred tax adjustment

All figures are TTM, from the cash flow statement unless stated.

1. Take the "Deferred income taxes" line (Q3 2026: $36.3B; a year earlier: $9.0B).
2. Remove the Anthropic piece. Unrealized gains on the Anthropic investments are booked in non-operating income, which the cash flow statement removes from OCF ("Non-operating expense (income), net"). The tax on those gains is deferred and added back. The two cancel out, so this piece is neutral for OCF and is not a boost. Estimate it from the 10-Q income tax note ("net discrete tax expense primarily attributable to the upward adjustments to our investments in Anthropic"; $15.2B for the first nine months of 2026, $0.35B for the same period of 2025), or at about 21-25% of the TTM Anthropic gains if the note gives no figure.
3. The rest is the real tax deferral (Q3 2026: about $21B, against about $7B a year earlier).
4. The temporary part is the real deferral minus the level of a year earlier, taken as the normal level (Q3 2026: about $14B).
5. Subtract the temporary part from reported OCF.

This is an estimate. The 10-Q does not give the exact split, so the result can be a few billion off. Say so in the quarterly file. A $1B error on the base moves the fair price by about $2.

Worked example, Q3 2026: 168.3 - 14.0 (deferred taxes) - 19.9 (SBC) = 134.4 $B.

## Stock-specific points to watch

- **Anthropic:** large non-cash gains inflate net income (so do not use net income for ratios). Revenue from AWS deals with AI labs that Amazon also finances is a concentration risk.
- **Capex:** about $220B planned for 2026. All the OCF goes to capex, and FCF is negative. Debt has risen from $65.6B (end of 2025) to $173.1B (Q3 2026).
- **AWS:** TTM operating margin and growth are the main drivers of the growth assumptions (management projects growth above 40% in 2027 and 2028).
- **Prime Day timing:** it moves between Q2 and Q3, so compare the two quarters together.
