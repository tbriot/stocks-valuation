---
name: adobe-quarterly-results
description: Download Adobe's (ADBE) quarterly financial documents (10-Q, Earnings Press Release, Earnings Script and Slides, Transcript and Investor Datasheet as PDFs, or 10-K for Q4) from the Adobe Investor Relations site and save them under adbe/documents/earnings/<fiscal year> Q<n>/. Use when the user asks for Adobe's or ADBE's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Adobe quarterly results

The IR page `https://www.adobe.com/investor-relations/financial-documents.html` is static HTML: one `h2` per fiscal year, one `h3` per quarter, and the PDF links under each. The file names contain random strings, so they cannot be guessed: the script reads them from the page.

## What is downloaded

| Link label on the page | Local file name |
|---|---|
| Form 10-Q (Form 10-K for Q4) | `ADBE-<year>-Q<n>-10-Q.pdf` (`-10-K.pdf` for Q4) |
| Earnings press release | `ADBE-<year>-Q<n>-Press-Release.pdf` |
| Earnings script and slides | `ADBE-<year>-Q<n>-Script-Slides.pdf` |
| Earnings transcript | `ADBE-<year>-Q<n>-Transcript.pdf` |
| Investor datasheet | `ADBE-<year>-Q<n>-Investor-Datasheet.pdf` |

The webcast is a link to a player: skipped. Not every quarter has every document (the datasheet exists only from 2026 Q2; the transcript can appear a day or two after the release); a missing one is reported, not an error.

## Fiscal calendar

Year and quarter are **Adobe's fiscal ones** (the fiscal year ends the Friday closest to November 30). Q1 ends about end of February, Q2 about end of May, Q3 about end of August, Q4 about end of November / early December. Adobe reports about 2-3 weeks after quarter end (Q3 in mid-September, Q4 and the 10-K in December-January).

## Target quarter

- Default: the latest quarter on the page (the first `h3` Q under the first fiscal year). If the user's date suggests a newer quarter not yet listed, say so.
- If the user names a quarter (for example "2026 Q1"), use that one.

## Procedure

Run from anywhere (the script finds the project root itself):

```
python3 .claude/skills/adobe-quarterly-results/download.py <fiscal_year> <quarter>
```

Existing files are never downloaded again ("already present"). Each file is checked to be a PDF and written through a temporary file. The script prints what was downloaded, already present, missing or in error. Then summarise: quarter, files downloaded, already present, missing, errors.

## If something goes wrong

- The site answers 403 to a custom or browser-like User-Agent (checked 2026-11-11: `ADBE valuation script` and a Mozilla string were refused), but accepts the client's default identity. So the script sends **no** User-Agent header of its own: do not add one. If it still answers 403 or shows a challenge page, stop and tell the user. Do not work around the protection (no browser headers or cookies).
- Never run `rm` (or any deletion) on a path built from a variable: Claude Code blocks it.
