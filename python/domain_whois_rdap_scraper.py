"""Domain WHOIS Lookup: expiry, registrar, age ($0.5/1K)

Domain WHOIS lookup over RDAP: registered flag, registrar, creation, expiry and update dates, days until expiry, domain age, status and nameservers. Takes a list of domain names. Use it to check domain expiry dates and domain availability in bulk.

Apify page: https://apify.com/tamnt67/domain-whois-rdap-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "domains": [
        "apify.com",
        "wikipedia.org",
        "stripe.com",
        "shopify.com",
        "notion.so"
    ]
}

run = client.actor("tamnt67/domain-whois-rdap-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
