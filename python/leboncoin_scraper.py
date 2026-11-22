"""Leboncoin Listings Scraper: France Classified Ads, Prices

Leboncoin listings scraper for leboncoin.fr classified ads: title, price, category, city, region, coordinates, seller type (pro or private), attributes and publish date. Takes keywords or any Leboncoin search URL with filters (France). Use it to track prices of cars, property or goods in France.

Apify page: https://apify.com/tamnt67/leboncoin-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "vélo électrique"
    ],
    "sortBy": "time",
    "maxItemsPerQuery": 50
}

run = client.actor("tamnt67/leboncoin-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
