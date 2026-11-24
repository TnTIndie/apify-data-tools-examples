"""Shopify Store Scraper: Theme, Apps & Tech Stack ($1.5/1K)

Shopify store scraper: theme, 45+ installed apps, tracking IDs, payment options, socials, location and product count, plus products with variants, collections and catalog stats. Takes store domains or product URLs. Use it to research competitors and qualify Shopify leads by app or theme.

Apify page: https://apify.com/tamnt67/shopify-store-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "mode": "store_detect",
    "domains": [
        "www.taylorstitch.com",
        "colourpop.com",
        "allbirds.com"
    ]
}

run = client.actor("tamnt67/shopify-store-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
