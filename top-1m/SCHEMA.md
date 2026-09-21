# Top 1 Million Websites — column reference

`top-1m.csv` (full file in Releases) · 1,000,000 rows · UTF-8 · comma-separated

| column | type | meaning |
|---|---|---|
| `rank` | integer, 1–1,000,000 | position by `linking_domains`, descending |
| `domain` | string | registrable domain, lowercase, no scheme, no `www.` |
| `linking_domains` | integer | number of **distinct** domains whose homepage links to it |

`sample-1000.csv` in this folder is the first 1,000 rows — same format.

## Notes

- `linking_domains` counts **domains, not links**: a site linking 500 times
  still counts once. This makes the metric resistant to link spam.
- Only **homepage** links are counted. The number is therefore a consistent
  lower bound, not a total backlink count.
- Ranks shift between monthly editions; cite the edition (or the release DOI)
  if you need a stable reference.
- The per-domain pages on piperic.com (`/links-to/<domain>`) let you inspect
  the linking domains behind any number here.
