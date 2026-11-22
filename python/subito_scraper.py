"""Subito.it Ads Scraper: Italy Classified Listings ($2/1K)

Subito ads scraper for Subito.it classified listings: title, description, price, category, condition, shipping, date, region, province, town, seller type and photos. Takes search terms or Subito.it search URLs (Italy). Use it to track prices of cars, property or goods in Italy.

Apify page: https://apify.com/tamnt67/subito-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "queries": [
        "iphone 15"
    ],
    "maxItems": 200
}

run = client.actor("tamnt67/subito-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
