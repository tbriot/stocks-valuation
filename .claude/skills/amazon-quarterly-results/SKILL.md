---
name: amazon-quarterly-results
description: Download Amazon's quarterly financial documents (Earnings Release, Presentation and 10-Q as PDFs, or 10-K for Q4) from the Amazon Investor Relations site and save them under amzn/documents/earnings/<year> Q<n>/. Use when the user asks for Amazon's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Amazon quarterly results

The page https://ir.aboutamazon.com/quarterly-results/default.aspx loads its list through a JSON feed. Query that feed directly: it is more reliable than reading the page, which is rendered with JavaScript (`WebFetch` sees none of the links).

## Feed

```
curl -sg "https://ir.aboutamazon.com/feed/FinancialReport.svc/GetFinancialReportList?apiKey=BF185719B0464B3CB809D23926182246&LanguageId=1&reportTypes=First%20Quarter|Second%20Quarter|Third%20Quarter|Fourth%20Quarter&tagList=&includeTags=true&excludeSelection=1&pageNumber=0&pageSize=<N>&year=<Y>"
```

(`apiKey` is the public key the site itself uses.)

The response holds `GetFinancialReportListResult`, a list of reports sorted from newest to oldest. Each report has `ReportYear`, `ReportSubType` (`First Quarter` … `Fourth Quarter`) and `Documents`. Each document has a `DocumentCategory` and a `DocumentPath` (the file URL).

Parameters to vary so you only fetch what you need:
- Latest quarter: `pageSize=1&year=-1`
- A specific quarter: `pageSize=-1&year=<year>` (3 to 4 reports), then filter on `ReportSubType`
- `year=-1&pageSize=-1` returns the whole history (~100 KB): avoid it.

## Documents to download

Only these, identified by `DocumentCategory` (do not rely on the title):

| DocumentCategory | Label on the site      | Local file name                          | Quarters |
|------------------|------------------------|------------------------------------------|----------|
| `news-pdf`       | Earnings Release (PDF) | `AMZN-<year>-Q<n>-Earnings-Release.pdf`  | all      |
| `presentation`   | Presentation (PDF)     | `AMZN-<year>-Q<n>-Presentation.pdf`      | all      |
| `tenq`           | 10-Q (PDF)             | `AMZN-<year>-Q<n>-10-Q.pdf`              | Q1-Q3    |
| `tenk`           | 10-K (PDF)             | `AMZN-<year>-Q4-10-K.pdf`                | Q4 only  |

Ignore everything else (`news`, `webcast`, etc.).
The original file names are unreliable (the 10-Q and 10-K are UUIDs), hence the imposed naming.

## Target quarter

- Default: the latest one (`pageSize=1&year=-1`, a single report returned).
- If the user names a quarter (e.g. "2026 Q1"), use the matching report.
- Mapping: `First Quarter`=Q1, `Second Quarter`=Q2, `Third Quarter`=Q3, `Fourth Quarter`=Q4.
- **Q4**: there is no 10-Q; Amazon publishes a 10-K (`tenk`) instead. Always download it (in addition to the Earnings Release and Presentation), and never look for a `tenq`.

## Destination

`amzn/documents/earnings/<year> Q<n>/` at the project root (e.g. `amzn/documents/earnings/2026 Q3/`; note the space, not a hyphen, as in the existing folders). Create the subdirectory if needed.

## Procedure

1. Call the feed, extract the target report and the URLs of the documents to download (3 documents: Earnings Release, Presentation, and 10-Q for Q1-Q3 or 10-K for Q4), with `python3` or `jq`.
2. For each document, if the local file already exists, **do not download it again** and report it as "already present".
3. Otherwise download it with `curl -fL -o "$tmp/<name>" <url>` into a temporary directory (`tmp=$(mktemp -d)`), never directly into the destination.
4. Check with `file` that the result is really a PDF. If so, `mv` it to the destination. If not, report the error and leave it in the temporary directory.
5. End with a summary: quarter, files downloaded, already present, missing (e.g. 10-Q not yet published), errors.

**Never run `rm` (or any deletion) on a path built from a variable**: Claude Code blocks it with a "Dangerous rm operation on possibly-empty variable path" warning. The temporary directory + `mv` flow above makes deletion unnecessary.

A document may be absent from a recent report (e.g. the 10-Q is not always published on the day of the results): report it without failing.

## If access is blocked

If the feed answers 403 or otherwise refuses: stop and tell the user. Do not work around the protection (no fake User-Agent or browser-like headers).
