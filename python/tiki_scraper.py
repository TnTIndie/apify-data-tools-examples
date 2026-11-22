"""Tiki Products Scraper: Tiki.vn Search, Categories, Details

Tiki products scraper: name, price, original price, discount, rating, review count, quantity sold, seller and brand. Takes keywords, category IDs or Tiki.vn URLs (Vietnam); full details add specifications, images, variants and stock. Use it to monitor prices and top sellers on Tiki.

Apify page: https://apify.com/tamnt67/tiki-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "tai nghe bluetooth"
    ],
    "sortBy": "top_seller",
    "maxItemsPerQuery": 45,
    "includeDetails": True
}

run = client.actor("tamnt67/tiki-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
