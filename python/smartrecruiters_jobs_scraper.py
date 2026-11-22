"""SmartRecruiters Jobs Scraper ($1/1K jobs)

SmartRecruiters jobs scraper: title, department, function, employment type, experience level, location, remote flag, posting date and full description. Takes SmartRecruiters company IDs (e.g. Bosch), with keyword and country filters. Use it to track roles at companies that hire on SmartRecruiters.

Apify page: https://apify.com/tamnt67/smartrecruiters-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "companies": [
        "BoschGroup",
        "https://jobs.smartrecruiters.com/Visa"
    ],
    "maxJobsPerCompany": 40,
    "includeDescription": True
}

run = client.actor("tamnt67/smartrecruiters-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
