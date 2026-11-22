"""AliExpress Products Scraper: Prices, Orders, Ratings

AliExpress products scraper: title, sale price, discount, star rating, number sold, images, ad flag and product URL. Takes keywords or AliExpress search URLs with your filters. Use it to find trending products and prices for dropshipping research.

Apify page: https://apify.com/tamnt67/aliexpress-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "wireless earbuds"
    ],
    "sortBy": "orders",
    "maxItemsPerQuery": 80
}

run = client.actor("tamnt67/aliexpress-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
