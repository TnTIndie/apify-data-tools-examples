"""Gupy Jobs Scraper: Brazil Job Openings ($1.5/1K jobs)

Gupy jobs scraper for Brazil job openings: title, company, department, city, state, workplace type (remote, hybrid, on-site), job type, publish date and full description. Takes keywords for the Gupy job portal or company career pages. Use it to track Brazilian hiring.

Apify page: https://apify.com/tamnt67/gupy-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "searchTerms": [
        "desenvolvedor",
        "engenheiro de dados"
    ],
    "workplaceType": "remote",
    "maxResults": 200,
    "includeDetails": True
}

run = client.actor("tamnt67/gupy-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
