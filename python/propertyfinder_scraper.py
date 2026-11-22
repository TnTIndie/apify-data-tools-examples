"""Property Finder Listings: UAE, Saudi, Qatar, Egypt ($0.8/1K)

Property Finder listings scraper: price, rent period, property type, bedrooms, bathrooms, size, location, coordinates, amenities, agency and photos. Takes search URLs or a country, purpose and type for the UAE, Saudi Arabia, Qatar, Bahrain and Egypt. Use it to track Dubai property prices.

Apify page: https://apify.com/tamnt67/propertyfinder-scraper
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
            "url": "https://www.propertyfinder.ae/en/search?c=1&l=1&ob=mr"
        }
    ],
    "maxItems": 100
}

run = client.actor("tamnt67/propertyfinder-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
