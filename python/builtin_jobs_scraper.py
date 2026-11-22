"""Built In Jobs Scraper: Tech & Startup Jobs ($1/1K)

Built In jobs scraper for builtin.com tech and startup jobs: title, company, location, remote or hybrid, salary range, seniority, industry, summary and top skills. Takes keywords, a remote-only switch or Built In search URLs. Use it to track startup hiring and tech salaries.

Apify page: https://apify.com/tamnt67/builtin-jobs-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "queries": [
        "product manager"
    ],
    "remoteOnly": True,
    "maxPagesPerSearch": 3,
    "maxItems": 120
}

run = client.actor("tamnt67/builtin-jobs-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
