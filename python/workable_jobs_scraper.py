"""Workable Jobs Scraper ($1/1K jobs)

Workable jobs scraper: title, department, function, employment type, location, remote flag, posting date and full description. Takes Workable company account names or apply.workable.com career page URLs, with title and location filters. Use it to track open roles at companies that hire on Workable.

Apify page: https://apify.com/tamnt67/workable-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "companies": [
        "huggingface",
        "https://apply.workable.com/blueground"
    ],
    "includeDescription": True
}

run = client.actor("tamnt67/workable-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
