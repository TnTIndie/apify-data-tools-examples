"""ATS Jobs Scraper (Greenhouse, Lever, Ashby, Recruitee)

Greenhouse jobs, Lever jobs, Ashby jobs and Recruitee jobs scraper: title, department, location, remote flag, employment type, salary where published, posting date and description. Takes company job board names, with title, location and date filters. Use it to track hiring at target companies.

Apify page: https://apify.com/tamnt67/ats-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "companies": [
        "https://boards.greenhouse.io/stripe",
        "https://jobs.lever.co/spotify",
        "https://jobs.ashbyhq.com/openai"
    ],
    "maxJobsPerCompany": 40
}

run = client.actor("tamnt67/ats-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
