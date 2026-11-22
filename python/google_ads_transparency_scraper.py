"""Google Ads Transparency Scraper (ads, advertisers, regions)

Google Ads Transparency Center scraper for Google ads: advertiser name and ID, creative ID, ad format, first and last shown dates, image or preview link and ad URL. Takes advertiser names, AR IDs or website domains, with country, format and date filters. Use it to research competitor ads.

Apify page: https://apify.com/tamnt67/google-ads-transparency-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "advertisers": [
        "https://adstransparency.google.com/advertiser/AR16735076323512287233"
    ],
    "regions": [
        "DE"
    ],
    "format": "any",
    "includeDetails": True,
    "maxAdsPerQuery": 45,
    "domains": []
}

run = client.actor("tamnt67/google-ads-transparency-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
