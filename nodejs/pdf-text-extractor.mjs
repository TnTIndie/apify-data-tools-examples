// PDF Text Extractor: PDF URL to Text, per Page ($2/1K)
// PDF text extractor: full text per PDF or per page, page count, word count, file size and metadata (title, author, dates). Takes PDF URLs, nothing to upload. Use it to turn PDF documents into text for search or LLM input.
// Apify page: https://apify.com/tamnt67/pdf-text-extractor
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "pdfUrls": [
        "https://arxiv.org/pdf/1706.03762",
        "https://www.irs.gov/pub/irs-pdf/fw9.pdf"
    ],
    "outputMode": "page"
};

const run = await client.actor('tamnt67/pdf-text-extractor').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
