"""Flipkart Products Scraper: Prices, Discounts, Ratings

Flipkart products scraper: title, brand, price, MRP, discount, rating, rating and review counts, stock and Flipkart Assured flag. Takes keywords or Flipkart search and category URLs (India). Use it to track Flipkart prices and discounts or compare products in a category.

Apify page: https://apify.com/tamnt67/flipkart-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "wireless earphones"
    ],
    "sortBy": "popularity",
    "maxItemsPerQuery": 60
}

run = client.actor("tamnt67/flipkart-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
