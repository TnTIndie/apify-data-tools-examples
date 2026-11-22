"""Zillow Listings Scraper: Homes for Sale and Rent

Zillow listings scraper for homes and properties: price, beds, baths, living area, address, home type, listing status, days on Zillow and Zestimate. Takes any zillow.com search URL with your filters (for sale, for rent, sold; city, ZIP or map). Use it to analyze US home prices and rentals.

Apify page: https://apify.com/tamnt67/zillow-scraper
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
            "url": "https://www.zillow.com/austin-tx/rentals/"
        }
    ],
    "maxItemsPerUrl": 60
}

run = client.actor("tamnt67/zillow-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
