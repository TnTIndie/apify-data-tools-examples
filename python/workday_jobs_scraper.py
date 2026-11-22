"""Workday Jobs Scraper ($1/1K jobs)

Workday jobs scraper for myworkdayjobs.com career sites: title, location, job ID, posting date, time type, remote type and full description. Takes the Workday career site URLs of any company. Use it to track open roles at large employers.

Apify page: https://apify.com/tamnt67/workday-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "careerSites": [
        "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite",
        "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site"
    ],
    "maxJobsPerSite": 40,
    "includeDetails": True
}

run = client.actor("tamnt67/workday-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
