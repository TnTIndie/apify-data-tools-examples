"""Website Screenshot: Full Page, PNG/JPEG, Bulk ($2.5/1K)

Website screenshot capture with real Chrome: screenshot download link, page title, final URL, HTTP status, image size and format. Takes a list of URLs, full page or visible area, PNG or JPEG, any viewport width (desktop or mobile). Use it to archive web pages or check how sites render.

Apify page: https://apify.com/tamnt67/website-screenshot
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "urls": [
        "https://apify.com",
        "https://www.wikipedia.org"
    ],
    "fullPage": True,
    "format": "jpeg"
}

run = client.actor("tamnt67/website-screenshot").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
