# MA — stock-specific process

General rules are in `../valuation-process.md`. This file holds what is specific to MA (Mastercard).

## Ratio and metric

Price / Free Cash Flow (FCF), TTM.

FCF = net cash provided by operating activities - purchases of property and equipment - capitalized software. Mastercard does not report a FCF line in its earnings release (checked on the Q3 2026 release and presentation), so compute it from the cash flow statement. Say in the quarterly file that this is my computation.

History of the method (see `valuations/2025-archive.md`):
- May 2025: first valuation, on earnings (P/E). Fair price $425, then $450 after the TTM update, with unchanged growth and end multiples.
- June 2026 (Q1 2026 results): switched to P/FCF TTM. Fair price $490 (previously $450) with the same growth and end multiples. The archive does not record the growth rates and end multiples themselves; ask me for them before the first quarterly file.

Why FCF and not earnings: the company is asset-light, so capex is small (nine months of 2026: $1.1B against $11.9B of OCF) and FCF is close to OCF. It is the cash that can be returned to shareholders, and buybacks are large.

Decision of 2026-11-03: keep P/FCF rather than going back to P/E. The FCF is the cash available for buybacks, and it includes the customer incentives that are paid in cash upfront and expensed slowly. Changing the ratio because the FCF lagged earnings would be a bias. Use the P/E (Q3 2026: 33.2 on TTM GAAP net income of $16,958M) and the FCF / net income ratio (TTM 91%; nine months of 2026 83% against 107% in 2025) as a cross-check in section 1 of the quarterly file.

Reference multiples (Q1 2026 note, financecharts.com, reported FCF): P/FCF 25.7 at the time; 10-year median 37, min 24, max 62. It was that low only three times in ten years (2016, 2020, 2022). Earlier P/E reference (May 2025): 15-year median 28, current 40. These are a rough guide for end multiples. Ratios computed here may differ from public ones because of the FCF definition.

No adjustment is made for stock-based compensation (SBC): decided, because it is small (nine months of 2026: $525M, about 4% of OCF). The metric is the reported FCF as defined above. Revisit it if SBC grows noticeably as a share of OCF; the risk indicators table tracks it. Without the SBC adjustment, dilution is not paid for in the base, so the buybacks (see "Dilution and buybacks") and the year-over-year change in shares matter more.

Assumptions after Q3 2026 (pessimistic / neutral / optimistic), given on FCF: 5-year growth 9% / 13% / 16%, end P/FCF 18 / 25 / 32. Fair price $470. They are my own judgment. The neutral growth is set below the revenue and consensus-based earnings growth because the FCF margin is depressed (42.5% TTM against 50.1% in 2025) and customer incentives grow faster than revenue; the guidance (revenue at the high end of low double digits, expenses growing at the same pace) gives no margin leverage in 2026.

## Where to find the data

Earnings release (page 9 of the Q3 2026 release, to be confirmed against the PDF, "Consolidated Statements of Cash Flows"): the columns are the year to date, so TTM = last 10-K year - prior year to date + current year to date. Lines: net cash provided by operating activities, purchases of property and equipment, capitalized software, share-based compensation, purchases of treasury stock, dividends, acquisitions, proceeds from and payment of debt. The balance sheet is on the page before: debt, cash, investments.

10-Q:
- Note 9 (debt) and "Liquidity and Capital Resources" in the MD&A: debt, credit facilities, buyback authorization.
- Note 10 (stockholders' equity): share repurchases and share count.
- Note 12 (share-based payments): grants and compensation cost.
- Note 14 (legal and regulatory proceedings): litigation and settlements, a recurring risk for MA.
- Note 17 (segment reporting).

Presentation and Supplemental Operational Performance Data: payment network and value-added services growth, volumes (gross dollar volume, cross-border), and guidance.

## Stock-specific points to watch

- **Revenue growth and guidance:** revenue growth was +17% in the quarter reported on 31/05/2025 (labelled Q2 2025 in the archive, probably Q1 2025; adjusted EPS +16%), +12% in Q1 2026 (a slowdown?), +14% in Q3 2026. Guidance for FY2026: "high end of low double digits". Adjusted diluted EPS growth stays higher (+18% in Q1 2026) thanks to margins and buybacks.
- **Segments:** payment network (+11% in Q3 2026, +8% in Q1 2026) against value-added services and solutions (+19% in Q3 2026, +18% in Q1 2026). The mix drives the margin; the value-added services share keeps rising.
- **Customer incentives and prepaid expenses:** "Prepaid expenses" is the largest working capital outflow ($4.7B over nine months of 2026, $2.9B a year earlier), and rebates and incentives grow faster than the network revenue (+18% in Q3 2026). Check that the TTM FCF is not depressed or flattered by the timing of these payments; nine-month OCF fell from $12.6B to $11.9B while net income rose from $10.9B to $12.9B. Treat any working capital swing as a possible one-off to normalize (Step 5, point 5 of the general process) and tell me before adjusting.
- **Litigation and settlements:** accrued litigation moved by -$0.5B in the nine months of 2026. Large payments hit OCF but may be one-offs.
- **Buybacks and dilution:** buybacks are heavy ($11.9B over nine months of 2026, $3.0B in Q3 2026, against $8.2B a year earlier), often above the OCF of the quarter, so cash and debt absorb the difference (Q1 2026: $4B of buybacks against about $3B of OCF). Dividend yield is about 0.2-0.5%, negligible. The share count falls, which supports EPS and FCF per share. Use the share count of the latest filing and check the year-over-year change. SBC is not subtracted from FCF, so use the actual share count and its year-over-year change, without any extra dilution assumption.
- **Debt and acquisitions:** proceeds from debt $5.6B and acquisitions $1.4B over nine months of 2026. Track debt over TTM FCF and net debt in the risk indicators table. Debt is financing the buybacks and deals, which lowers the end multiple if it keeps growing.
- **Multiple risk:** in May 2025 the P/E was 40 against a 15-year median of 28, so the stock was expensive against its history. The end multiples carry most of the uncertainty; compare with Visa (in May 2025: slightly lower growth but a lower multiple, 33 against 38 for MA).
- **Regulation:** read the legal and regulatory note of the 10-Q each quarter (Note 14) for new proceedings.
