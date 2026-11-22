"""Netflix Prices by Country Scraper ($2/1K plans)

Netflix prices by country: plan name, price, price text, currency, billing period, ads flag and extra member prices. Takes country codes, or all countries, and reads Netflix's official Plans and Pricing help pages. Use it to compare Netflix subscription prices worldwide.

Apify page: https://apify.com/tamnt67/netflix-prices-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "countries": [
        "US",
        "GB",
        "IN",
        "BR",
        "DE",
        "JP",
        "VN"
    ]
}

run = client.actor("tamnt67/netflix-prices-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
