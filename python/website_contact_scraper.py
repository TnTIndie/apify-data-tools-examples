"""Website Contact Scraper (emails, phones, social links)

Website contact scraper: emails, phone numbers and social links (LinkedIn, Facebook, Instagram, X, YouTube, TikTok) for each site. Takes a list of domains or URLs and checks the homepage plus contact, about and imprint pages. Use it to build lead lists with email addresses from company websites.

Apify page: https://apify.com/tamnt67/website-contact-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "websites": [
        "apify.com",
        "https://crawlee.dev"
    ],
    "maxPagesPerSite": 5
}

run = client.actor("tamnt67/website-contact-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
