"""App Store Search Scraper: ASO Keyword Ranks ($1/1K apps)

App Store search scraper for ASO keyword rankings: rank, app name, developer, price, rating, rating count, genre, version, update date and description. Takes keywords and App Store countries. Use it to see which iOS apps rank for a keyword and track your app's rank.

Apify page: https://apify.com/tamnt67/app-store-search-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "habit tracker",
        "meal planner",
        "vpn"
    ],
    "countries": [
        "us",
        "gb"
    ],
    "maxAppsPerKeyword": 50
}

run = client.actor("tamnt67/app-store-search-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
