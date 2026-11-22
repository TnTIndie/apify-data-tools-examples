"""GitHub Trending Repositories Scraper ($0.8/1K)

GitHub trending repositories scraper: rank, repository name, owner, description, language, stars, forks, stars gained in the period and contributors. Takes periods (today, this week, this month) and programming languages. Use it to spot fast-growing open source projects.

Apify page: https://apify.com/tamnt67/github-trending-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "periods": [
        "weekly"
    ],
    "languages": [
        "all",
        "python"
    ]
}

run = client.actor("tamnt67/github-trending-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
