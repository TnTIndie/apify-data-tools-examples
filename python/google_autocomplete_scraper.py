"""Google Autocomplete Keyword Scraper ($1/1K keywords)

Google Autocomplete keyword suggestions scraper: seed keyword, suggestion, modifier, position, word count, language and country. Takes seed keywords and expands them with A to Z and question words. Use it for SEO keyword research and long-tail keyword ideas.

Apify page: https://apify.com/tamnt67/google-autocomplete-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "coffee machine"
    ],
    "language": "en",
    "country": "us",
    "expandAlphabet": True,
    "expandQuestions": True,
    "maxSuggestionsPerKeyword": 500
}

run = client.actor("tamnt67/google-autocomplete-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
