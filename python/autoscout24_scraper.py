"""AutoScout24 Car Listings Scraper

AutoScout24 car listings scraper: make, model, price, mileage, first registration, fuel, gearbox, power, seller type and location. Takes any AutoScout24 search URL with your filters (.com, .de, .it, .fr, .es, .nl, .be, .at). Use it to compare used car prices across Europe.

Apify page: https://apify.com/tamnt67/autoscout24-scraper
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
            "url": "https://www.autoscout24.com/lst/bmw/3-series?atype=C&cy=D&sort=standard&desc=0"
        }
    ],
    "sortBy": "url",
    "maxItemsPerUrl": 50
}

run = client.actor("tamnt67/autoscout24-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
