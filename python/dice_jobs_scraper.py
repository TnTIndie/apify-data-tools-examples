"""Dice Jobs Scraper: US Tech Jobs ($0.9/1K jobs)

Dice jobs scraper for US tech jobs: title, company, location, salary, employment type, posting date, Easy Apply flag and link; optional full description. Takes keywords and location or Dice.com search URLs. Use it to track tech job listings and salaries in the US.

Apify page: https://apify.com/tamnt67/dice-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "queries": [
        "data engineer"
    ],
    "includeDescription": True,
    "maxPagesPerSearch": 2,
    "maxItems": 80
}

run = client.actor("tamnt67/dice-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
