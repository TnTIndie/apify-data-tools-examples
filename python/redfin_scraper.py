"""Redfin Listings Scraper: US Homes for Sale ($1/1K homes)

Redfin listings scraper for homes for sale: price, beds, baths, square feet, price per sq ft, year built, address, coordinates, days on market and last sold date. Takes Redfin city, county or neighborhood URLs (US), with price and bedroom filters. Use it to analyze US real estate listings.

Apify page: https://apify.com/tamnt67/redfin-scraper
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
            "url": "https://www.redfin.com/city/30818/TX/Austin"
        }
    ],
    "maxItems": 200
}

run = client.actor("tamnt67/redfin-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
