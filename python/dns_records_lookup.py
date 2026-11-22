"""DNS Records Lookup: MX, SPF, DMARC, A, TXT ($0.5/1K)

DNS records lookup: A, AAAA, CNAME, MX, NS, TXT, SOA and CAA records, plus mail provider, SPF record and DMARC policy. Takes a list of domains and queries public DNS over HTTPS. Use it to check MX records and email deliverability setup (SPF, DMARC) for many domains.

Apify page: https://apify.com/tamnt67/dns-records-lookup
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
        "github.com",
        "stripe.com",
        "shopify.com",
        "proton.me"
    ],
    "checkEmailSecurity": True
}

run = client.actor("tamnt67/dns-records-lookup").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
