"""Y Combinator Companies Scraper + Jobs ($1/1K)

Y Combinator companies scraper for YC startups: name, batch, status, industry, team size, location, website, social links and open jobs with salary ranges. Takes batches, industries, locations, keywords, status and a hiring-only switch. Use it to build startup lead lists or find YC jobs.

Apify page: https://apify.com/tamnt67/yc-companies-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "batches": [
        "W25",
        "Summer 2025"
    ],
    "hiringOnly": True,
    "maxResults": 150,
    "includeDetails": True
}

run = client.actor("tamnt67/yc-companies-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
