#!/usr/bin/env python3
"""Load either Piperic dataset and print a quick summary. Requires: pandas"""
import pandas as pd

# AI Crawler Registry (in this repo)
bots = pd.read_csv("ai-crawlers/ai-crawlers.csv")
print("AI crawlers:", len(bots))
print(bots.groupby("purpose").size().sort_values(ascending=False), "\n")

# Top 1M — pandas reads the gzipped file directly (or use the sample)
top = pd.read_csv("top-1m/top-1m.csv.gz")   # top-1m/sample-1000.csv for a quick look
print(top.head(10).to_string(index=False))
