"""FDA Drug Safety & Clinical Trials Scraper ($3/1K)

FDA and ClinicalTrials.gov scraper: trials with sponsor, phase, status, enrollment, eligibility, sites; FDA drug labels, FAERS adverse events, recalls and label interaction checks. Takes drug names, conditions, filters, NCT IDs or a search URL. Use it to track pharma pipelines and drug safety.

Apify page: https://apify.com/tamnt67/fda-clinical-trials-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "mode": "trials_search",
    "condition": "obesity",
    "limit": 50
}

run = client.actor("tamnt67/fda-clinical-trials-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
