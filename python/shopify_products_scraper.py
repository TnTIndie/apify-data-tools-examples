"""Shopify Products Scraper (prices, variants, stock)

Shopify products scraper: title, vendor, product type, tags, price, compare-at price, variants with SKUs, availability and images. Takes Shopify store domains or collection URLs. Use it to monitor a competitor store's catalog, prices and discounts.

Apify page: https://apify.com/tamnt67/shopify-products-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "stores": [
        "https://www.allbirds.com",
        "brooklinen.com"
    ],
    "maxProductsPerStore": 40
}

run = client.actor("tamnt67/shopify-products-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
