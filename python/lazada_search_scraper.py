"""Lazada & Daraz Products Scraper: Vietnam, Thailand, S. Asia

Lazada products and Daraz products scraper: name, price, discount, rating, review count, sold count, seller and brand. Takes keywords or search, category and brand URLs for Lazada Vietnam and Thailand and Daraz Pakistan, Bangladesh, Sri Lanka, Nepal and Myanmar. Use it to track prices and sellers.

Apify page: https://apify.com/tamnt67/lazada-search-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "air fryer"
    ],
    "country": "th",
    "sortBy": "popularity",
    "maxItemsPerQuery": 80
}

run = client.actor("tamnt67/lazada-search-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
