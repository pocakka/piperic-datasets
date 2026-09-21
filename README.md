# Piperic Open Datasets

Free, openly licensed datasets about the live web — published by
[Piperic](https://piperic.com), an independent index of 50M+ live,
content-validated websites.

**License: [CC BY 4.0](LICENSE)** — use them anywhere, including commercially,
just credit Piperic.

| Dataset | Rows | Files | Also on |
|---|---|---|---|
| **[Top 1 Million Websites](top-1m/)** | 1,000,000 | [top-1m.csv.gz](top-1m/top-1m.csv.gz) (9 MB) · [1,000-row sample](top-1m/sample-1000.csv) | [HuggingFace](https://huggingface.co/datasets/piperic/piperic-top-1m) · [Kaggle](https://www.kaggle.com/datasets/attilarczakcosi/piperic-top-1m) |
| **[AI Crawler Registry](ai-crawlers/)** | 969 | [ai-crawlers.csv](ai-crawlers/ai-crawlers.csv) | [HuggingFace](https://huggingface.co/datasets/piperic/piperic-ai-crawlers) · [Kaggle](https://www.kaggle.com/datasets/attilarczakcosi/piperic-ai-crawlers) |

---

## Top 1 Million Websites

The top 1,000,000 websites ranked by **how many distinct domains link to them
from their homepages** — a popularity signal that is hard to game, because each
linking domain counts once no matter how many links it places.

```
rank,domain,linking_domains
1,"facebook.com",17068124
2,"instagram.com",16064133
```

A link-evidence alternative to traffic-based lists. Updated monthly.
Live version and full context: https://piperic.com/tools/top-sites

> The full file ships gzipped (`top-1m.csv.gz`, 9 MB → 26 MB uncompressed).
> [`top-1m/sample-1000.csv`](top-1m/sample-1000.csv) shows the exact format
> without unpacking anything.
>
> ```bash
> gunzip -c top-1m/top-1m.csv.gz | head
> ```

## AI Crawler Registry

**969 AI crawlers and AI-adjacent bots** — operator, purpose (training vs.
answer vs. agent), robots.txt compliance, user-agent patterns and verification
hints, each row carrying its source attribution.

Useful for writing a robots.txt AI policy, analysing your access logs, or
researching how AI crawling evolves. Live version with per-bot pages and a
policy generator: https://piperic.com/tools/ai-bots

## Examples

- [`examples/load_pandas.py`](examples/load_pandas.py) — load either dataset, print the top rows
- [`examples/robots_policy.py`](examples/robots_policy.py) — generate a robots.txt that allows AI *answers* but blocks *training*

## Citing

If you use these datasets in research or a publication, please cite the
release DOI (see the badge above once the first release is archived), or:

> Piperic Open Datasets, Piperic Business Intelligence, https://piperic.com —
> CC BY 4.0.

## About the data

Piperic continuously crawls the homepages of 50M+ live websites (HTTP 2xx,
parked and dead domains removed) and maintains a link graph of 180M+ edges.
These datasets are **published outputs** of that index — the crawling and
classification systems themselves are proprietary.

Questions, corrections, or a custom cut (by country, technology or industry):
**hello@piperic.com**
