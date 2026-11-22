"""Craigslist Listings Scraper: For Sale, Housing ($2/1K)

Craigslist listings scraper: title, price, neighbourhood, URL, post ID and, where shown, bedrooms, bathrooms and coordinates. Takes Craigslist search URLs, or cities, a section (for sale, housing, jobs, services, gigs, cars) and keywords. Use it to monitor local classified ads and rentals.

Apify page: https://apify.com/tamnt67/craigslist-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "cities": [
        "newyork"
    ],
    "category": "sss",
    "queries": [
        "bike"
    ],
    "maxItems": 200
}

run = client.actor("tamnt67/craigslist-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
