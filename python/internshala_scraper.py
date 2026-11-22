"""Internshala Internships & Jobs Scraper: India ($1.5/1K)

Internshala internships and jobs scraper: title, company, locations, work-from-home flag, stipend or salary, duration, experience, skills and posting age. Takes keywords and locations or Internshala search URLs (India). Use it to track internships and fresher jobs in India.

Apify page: https://apify.com/tamnt67/internshala-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "type": "internships",
    "keywords": [
        "python",
        "marketing"
    ],
    "maxItemsPerSearch": 50
}

run = client.actor("tamnt67/internshala-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
