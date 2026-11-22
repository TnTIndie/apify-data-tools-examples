"""Polymarket & Kalshi Odds Scraper ($1/1K markets)

Polymarket and Kalshi odds scraper for prediction markets: question, outcome, implied probability, bid, ask, last price, 24h change, volume, liquidity and end date. Takes keywords, the sources to read and a minimum volume. Use it to track prediction market odds on elections, sports or economics.

Apify page: https://apify.com/tamnt67/prediction-markets-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "sources": [
        "polymarket",
        "kalshi"
    ],
    "maxMarketsPerSource": 60,
    "includeRules": False
}

run = client.actor("tamnt67/prediction-markets-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
