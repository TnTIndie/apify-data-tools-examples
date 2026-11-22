"""App Store Reviews Scraper (iOS ratings, text, any country)

App Store reviews scraper for iOS apps: star rating, title, text, author, app version, helpful votes and date, plus app rating and developer. Takes app IDs or Apple App Store URLs and a list of countries. Use it to track iPhone app ratings and user feedback.

Apify page: https://apify.com/tamnt67/app-store-reviews-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "appIds": [
        "324684580"
    ],
    "countries": [
        "us",
        "gb"
    ],
    "sortBy": "mostrecent",
    "maxReviewsPerApp": 120
}

run = client.actor("tamnt67/app-store-reviews-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
