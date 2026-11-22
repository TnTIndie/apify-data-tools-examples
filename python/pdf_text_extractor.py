"""PDF Text Extractor: PDF URL to Text, per Page ($2/1K)

PDF text extractor: full text per PDF or per page, page count, word count, file size and metadata (title, author, dates). Takes PDF URLs, nothing to upload. Use it to turn PDF documents into text for search or LLM input.

Apify page: https://apify.com/tamnt67/pdf-text-extractor
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "pdfUrls": [
        "https://arxiv.org/pdf/1706.03762",
        "https://www.irs.gov/pub/irs-pdf/fw9.pdf"
    ],
    "outputMode": "page"
}

run = client.actor("tamnt67/pdf-text-extractor").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
