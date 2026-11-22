"""Rakuten Products Scraper: Japan Prices, Points, Shops

Rakuten products scraper for Rakuten Ichiba Japan: name, price, Rakuten points, review score and count, shop, shipping fee, genre and URL. Takes keywords in Japanese or English, or rakuten.co.jp search and genre URLs. Use it to research prices and shops on Rakuten Japan.

Apify page: https://apify.com/tamnt67/rakuten-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "ワイヤレスイヤホン"
    ],
    "sortBy": "reviews",
    "maxItemsPerQuery": 60
}

run = client.actor("tamnt67/rakuten-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
