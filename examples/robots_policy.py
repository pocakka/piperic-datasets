#!/usr/bin/env python3
"""Build a robots.txt that ALLOWS AI answer/search bots but BLOCKS training bots.

Why this split: appearing in AI answers sends you traffic; being used as
training data does not. Many operators run separate crawlers for each, so the
choice is real — the `purpose` column is what makes it selectable.
"""
import csv

allow, block = [], []
for r in csv.DictReader(open("ai-crawlers/ai-crawlers.csv", encoding="utf-8")):
    if r["kind"] != "ai":
        continue
    (allow if r["purpose"] in ("answer", "search") else block).append(r["name"])

print("# Allow AI answers, block AI training — generated from the Piperic AI Crawler Registry")
print("# https://github.com/piperic/piperic-datasets\n")
for name in sorted(set(block)):
    print("User-agent: %s\nDisallow: /\n" % name)
for name in sorted(set(allow)):
    print("User-agent: %s\nAllow: /\n" % name)
print("# %d blocked, %d allowed" % (len(set(block)), len(set(allow))))
