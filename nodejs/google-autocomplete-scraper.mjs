// Google Autocomplete Keyword Scraper ($1/1K keywords)
// Google Autocomplete keyword suggestions scraper: seed keyword, suggestion, modifier, position, word count, language and country. Takes seed keywords and expands them with A to Z and question words. Use it for SEO keyword research and long-tail keyword ideas.
// Apify page: https://apify.com/tamnt67/google-autocomplete-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "coffee machine"
    ],
    "language": "en",
    "country": "us",
    "expandAlphabet": true,
    "expandQuestions": true,
    "maxSuggestionsPerKeyword": 500
};

const run = await client.actor('tamnt67/google-autocomplete-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
