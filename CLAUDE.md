# Stock valuation repository

Quarterly 5-year scenario valuation of stocks (portfolio and watchlist).

## Where to start

- For any request about a quarterly update or valuation, read `valuation-process.md` first (general rules), then `<ticker>/process.md` (stock-specific rules), then the latest file in `<ticker>/valuations/` as the template to follow.
- Layout of each stock folder: see "Repository layout" in `valuation-process.md`.
- For AMZN, the `amazon-quarterly-results` skill downloads the earnings release, presentation and 10-Q/10-K into `amzn/documents/earnings/<year> Q<n>/`. If those files are missing for the quarter, run it before starting the update.
- For GOOG, the `alphabet-quarterly-results` skill does the same into `goog/documents/earnings/<year> Q<n>/`.
- For MA, the `mastercard-quarterly-results` skill does the same into `ma/documents/earnings/<year> Q<n>/`.
- For CSU, the `constellation-quarterly-results` skill downloads the MD&A, the financial statements and the shareholder report (PDF, IFRS, in USD; there is no 10-Q) into `csu/documents/earnings/<year> Q<n>/`.
- For FTNT, the `fortinet-quarterly-results` skill downloads the 10-Q/10-K and the press release from SEC EDGAR into `ftnt/documents/earnings/<year> Q<n>/`, as HTML (not PDF). The presentation, prepared remarks and supplemental financials are not scriptable (the IR site blocks scripts): the user downloads them by hand.
- For BKNG, the `booking-quarterly-results` skill downloads the press release, presentation, prepared remarks, transcript and 10-Q/10-K (PDF) from the Booking Holdings IR site into `bkng/documents/earnings/<year> Q<n>/`. `bkng/process.md` is still a skeleton: the ratio and metric have to be chosen with me before the first valuation.

## How to work

- The growth rates, end multiples and fair price are my own judgment. Propose values with reasons, and wait for my confirmation before treating them as final.
- The fair price must follow the rule in Step 4 of `valuation-process.md`. Show the CAGRs for nearby prices.
- Compute every figure with Python and cross-check it against the previous quarter's file. Do not write numbers from memory.
- State clearly what is an estimate (for example the deferred tax adjustment) and what comes from the filings.
- The current share price comes from the `stock-quote` skill, with a web search as fallback. Give the source and the date. Do not ask me to confirm it.
- This is a git repository, meant to be pushed to a public GitHub repo: never write anything about my holdings (share counts, positions, cost basis, accounts). Source documents (`*/documents/`) are git-ignored. Commit only when I ask.
- Do not delete or overwrite my files without asking. Prefer adding new files and keeping the old ones.

## Language and format

- `valuation-process.md`, `process.md` files and this file are in English.
- Quarterly notes (`<ticker>/valuations/*.md`) are in French, in the format of the latest file.
- Number format in quarterly notes: space as thousands separator and comma as decimal separator (for example 6 150 728 and 11,5 %).

## Reading the PDFs

- Extract the text of the PDFs to `/tmp` and read it from there. Use `pdftotext -layout` if installed, otherwise the Python library `pypdf`.
- The 10-Q is long (hundreds of pages in the extracted text). Search it with grep for the passages needed instead of reading it all.
