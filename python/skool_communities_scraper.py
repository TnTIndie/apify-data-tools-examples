"""Skool Communities Scraper ($2/1K communities)

Skool communities scraper: name, URL, description, member count, paid flag, price, rating and review count. Takes search keywords for the public Skool discovery page. Use it to research Skool groups in a niche and their pricing.

Apify page: https://apify.com/tamnt67/skool-communities-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "searchQueries": [
        "ai automation"
    ],
    "maxResultsPerQuery": 60
}

run = client.actor("tamnt67/skool-communities-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
