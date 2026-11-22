// Domain WHOIS Lookup: expiry, registrar, age ($0.5/1K)
// Domain WHOIS lookup over RDAP: registered flag, registrar, creation, expiry and update dates, days until expiry, domain age, status and nameservers. Takes a list of domain names. Use it to check domain expiry dates and domain availability in bulk.
// Apify page: https://apify.com/tamnt67/domain-whois-rdap-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "domains": [
        "apify.com",
        "wikipedia.org",
        "stripe.com",
        "shopify.com",
        "notion.so"
    ]
};

const run = await client.actor('tamnt67/domain-whois-rdap-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
