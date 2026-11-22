"""Hepsiburada Products Scraper: Prices, Ratings, Sellers

Hepsiburada products scraper: name, brand, price, original price, discount rate, rating, review count, merchant and stock. Takes keywords or Hepsiburada search and category URLs (Turkey). Use it to monitor Turkish e-commerce prices and sellers.

Apify page: https://apify.com/tamnt67/hepsiburada-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "bluetooth kulaklık"
    ],
    "sortBy": "coklusatis",
    "maxItemsPerQuery": 50
}

run = client.actor("tamnt67/hepsiburada-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
