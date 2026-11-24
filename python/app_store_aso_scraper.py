"""App Store ASO Keyword Scraper: Difficulty & Ranks ($2/1K)

App Store ASO keyword scraper: difficulty and opportunity scores, top 10 ranked apps, related keywords and your app's rank, plus search results, app details, reviews and top charts. Takes keywords, app IDs or developer IDs and a country. Use it to pick ASO keywords and track app ranks.

Apify page: https://apify.com/tamnt67/app-store-aso-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "mode": "aso_keyword",
    "keywords": [
        "habit tracker",
        "budget planner",
        "meditation"
    ],
    "country": "us"
}

run = client.actor("tamnt67/app-store-aso-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
