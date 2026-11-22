"""Google Trends Trending Now Scraper ($2/1K trends)

Google Trends trending searches scraper: keyword, rank, approximate search volume, start time and linked news stories. Takes a list of countries and reads the Google Trends Trending Now feed. Use it to spot daily trending topics and keywords in any country.

Apify page: https://apify.com/tamnt67/google-trends-trending-scraper
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
        "IN"
    ],
    "maxItemsPerCountry": 100
}

run = client.actor("tamnt67/google-trends-trending-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
