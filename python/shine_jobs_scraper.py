"""Shine Jobs Scraper: Shine.com India ($1.5/1K jobs)

Shine jobs scraper for Shine.com in India: title, company, location, experience, salary in INR, skills, employment type, posting date and, with Include details, the full description. Takes keywords and a city or Shine.com search URLs. Use it to track Indian job listings and salaries.

Apify page: https://apify.com/tamnt67/shine-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "queries": [
        "python developer"
    ],
    "location": "Bangalore",
    "maxPagesPerSearch": 5,
    "maxItems": 100,
    "includeDetails": True
}

run = client.actor("tamnt67/shine-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
