"""Remote Jobs Scraper: 5 job boards in one ($1.5/1K jobs)

Remote jobs scraper for Remote OK, Jobicy, Himalayas, We Work Remotely and Arbeitnow: title, company, location, employment type, category, tags, salary where published, posting date and description. Takes keywords, sources and a posted-within limit. Use it to build a remote job feed.

Apify page: https://apify.com/tamnt67/remote-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "sources": [
        "remoteok",
        "jobicy",
        "himalayas",
        "weworkremotely",
        "arbeitnow"
    ],
    "maxJobsPerSource": 30,
    "includeDescription": True
}

run = client.actor("tamnt67/remote-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
