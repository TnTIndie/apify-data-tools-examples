"""Rightmove Property Listings Scraper: UK Sale & Rent ($1/1K)

Rightmove property listings scraper: price, bedrooms, bathrooms, property type, size, tenure, address, coordinates, first listed date and estate agent. Takes Rightmove search URLs for UK property for sale or to rent. Use it to track UK house prices and rentals.

Apify page: https://apify.com/tamnt67/rightmove-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "startUrls": [
        {
            "url": "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E904"
        }
    ],
    "maxPagesPerSearch": 5,
    "maxItems": 120
}

run = client.actor("tamnt67/rightmove-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
