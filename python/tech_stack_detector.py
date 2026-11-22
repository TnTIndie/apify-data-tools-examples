"""Website Tech Stack Detector: CMS, Analytics ($3/1K)

Website tech stack detector for website technologies: CMS, ecommerce platform, JavaScript framework, analytics, ad pixels, live chat, payments, CDN, hosting and server, with evidence. Takes a list of domains or URLs. Use it to find sites built with Shopify or WordPress for lead lists.

Apify page: https://apify.com/tamnt67/tech-stack-detector
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "urls": [
        "allbirds.com",
        "gymshark.com",
        "shopify.com",
        "squarespace.com",
        "wix.com"
    ],
    "maxConcurrency": 5
}

run = client.actor("tamnt67/tech-stack-detector").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
