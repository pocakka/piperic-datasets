# AI Crawler Registry — column reference

`ai-crawlers.csv` · 969 rows · UTF-8 · comma-separated, quoted

| column | meaning |
|---|---|
| `slug` | stable identifier, safe for URLs and joins |
| `name` | crawler name as its operator writes it |
| `operator` | the company or project running it |
| `kind` | `ai` = AI-specific · `crawler` = AI-adjacent (search, SEO, feeds) |
| `category` | grouping used on the live site (e.g. "AI Data Scrapers") |
| `purpose` | **the key column**: `training` · `answer` · `agent` · `search` · `other` |
| `respect` | does it honour robots.txt: `yes` · `no` · `unclear` |
| `major` | `True` for the widely-seen crawlers |
| `ua_patterns` | `\|`-separated substrings to match in a User-Agent header |
| `verify` | how to confirm identity: `rdns` · `ip-range` · `none` |
| `docs_url` | the operator's own documentation |
| `sources` | `\|`-separated provenance for this row |
| `description` | one-line summary |

## Notes

- Match `ua_patterns` **case-insensitively** as substrings, not as full strings.
- `purpose` is what makes a selective policy possible: many operators run
  separate bots for training and for answering, and you may want to allow one
  while blocking the other.
- `respect=no` means robots.txt alone will not stop it — you need server- or
  CDN-level rules.
- Updated weekly on piperic.com; this file is refreshed monthly.
