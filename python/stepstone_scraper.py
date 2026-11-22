"""StepStone Jobs Scraper (Germany, Austria, Belgium, NL)

StepStone jobs scraper: title, company, location, posting date, salary range, benefits, skills and job URL. Takes keywords and city or StepStone search URLs for Germany, Austria, Belgium and the Netherlands. Use it to track German job listings and salaries.

Apify page: https://apify.com/tamnt67/stepstone-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "python"
    ],
    "location": "Berlin",
    "sortBy": "date",
    "maxItemsPerSearch": 40
}

run = client.actor("tamnt67/stepstone-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
