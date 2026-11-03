---
name: mastercard-quarterly-results
description: Download Mastercard's (MA) quarterly financial documents (Earnings Release, Earnings Presentation, Supplemental Operational Performance Data and 10-Q as PDFs, or 10-K for Q4) from Mastercard's Investor Relations file host and save them under ma/documents/earnings/<year> Q<n>/. Use when the user asks for Mastercard's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Mastercard quarterly results

The IR site's list endpoint (`investor.mastercard.com/Services/FinancialReportService.svc/...`) is behind a Cloudflare challenge: **do not use it**. The PDF files themselves are served without protection by `s25.q4cdn.com`, under predictable but not fully regular names. So the URLs are built from candidates and checked one by one.

## Candidate URLs

Base: `B=https://s25.q4cdn.com/479285134/files`. With `YY` = last two digits of the year, `n` = quarter number, `Dir=$B/doc_financials/<year>/q<n>`. Try the candidates in order and keep the first one that answers 200 with a PDF.

| Document | Local file name | Candidates |
|---|---|---|
| Earnings Release | `MA-<year>-Q<n>-Earnings-Release.pdf` | `$Dir/<n>Q<YY>-Mastercard-Earnings-Release.pdf`, `$B/content_files/<n>Q<YY>-Mastercard-Earnings-Release.pdf`, `$Dir/<n>Q<YY>-Earnings-Release-Final.pdf`, `$Dir/<n>Q<YY>-Earnings-Release.pdf` |
| Presentation | `MA-<year>-Q<n>-Presentation.pdf` | `$Dir/<n>Q<YY>-Mastercard-Earnings-Presentation.pdf`, `$B/content_files/<n>Q<YY>-Mastercard-Earnings-Presentation.pdf`, `$Dir/<n>Q<YY>-Earnings-Presentation-Website.pdf`, `$Dir/<n>Q<YY>-Earnings-Presentation.pdf` |
| Supplemental data | `MA-<year>-Q<n>-Supplemental.pdf` | `$Dir/<n>Q<YY>-Mastercard-Supplemental-Operational-Performance-Data.pdf`, same name under `$B/content_files/` |
| 10-Q (Q1-Q3) | `MA-<year>-Q<n>-10-Q.pdf` | `$Dir/MA-<MM-DD>-<year>-10-Q-as-filed.pdf` with `<MM-DD>` = 03-31, 06-30, 09-30, then `$Dir/Mastercard-10-Q.pdf` (used for Q2 2026), then `$B/content_files/Mastercard-10Q-<n>Q-<YY>.pdf` (used for Q3 2026, latest quarter) |
| 10-K (Q4 only) | `MA-<year>-Q4-10-K.pdf` | `$Dir/MA-12-31-<year>-10-K-as-filed-with-standard-exhibits.pdf`, then `...-10-K-as-filed.pdf` |

Observed pattern (to extend if a new variant shows up): the latest quarter's documents first appear under `content_files/` and are later moved to `doc_financials/<year>/q<n>/`, so always try both. Some older quarters use other names (`-Final`, `-Website`) or a cloudfront URL for the 10-Q (for example Q3 2025: `https://d18rn0p25nwr6d.cloudfront.net/CIK-0001141391/bede9cc0-d964-41f7-a10b-995d8a3fdfb4.pdf`); those cannot be guessed, so ask the user for them. The Supplemental data is a secondary document: its absence is not an error.

Quarter mapping: Q1 = March 31, Q2 = June 30, Q3 = September 30, Q4 = December 31. **Q4**: there is no 10-Q, look for the 10-K instead.

## Target quarter

- Default: the latest quarter. Mastercard reports about 4 weeks after quarter end (Q3 results at the end of October). Start from the most recent quarter that has ended and step back until the Earnings Release is found.
- If the user names a quarter (e.g. "2026 Q1"), use that one.

## Destination

`ma/documents/earnings/<year> Q<n>/` at the project root (note the space, not a hyphen). Create it if needed.

## Procedure

1. For each document, if the local file already exists, **do not download it again**: report "already present".
2. Otherwise test the candidates in order: `curl -s -m 20 -o /dev/null -w '%{http_code}' <url>`. Take the first 200.
3. Download into a temporary directory (`tmp=$(mktemp -d)`) with `curl -fL -o "$tmp/<name>" <url>`, never directly into the destination.
4. Check with `file` that it is a PDF, then `mv` it to the destination. If not, report the error and leave it in the temporary directory.
5. Summarise: quarter, files downloaded, already present, missing, errors.

**Never run `rm` (or any deletion) on a path built from a variable**: Claude Code blocks it.

## If a document is missing

- Report it without failing (e.g. the 10-Q PDF is often not on q4cdn the day it is filed with the SEC).
- For a 10-Q/10-K, point to SEC EDGAR (CIK 1141391): `https://data.sec.gov/submissions/CIK0001141391.json` gives the filing dates and accession numbers (EDGAR requires a descriptive User-Agent with a contact e-mail, such as the user's address). It serves HTML, not PDF: do not download it unless the user asks.
- Ask the user for the URL if they have it, and add the variant to the table above.

## If access is blocked

If q4cdn answers 403 or shows a challenge page: stop and tell the user. Do not work around the protection (no fake User-Agent, browser headers or cookies).
