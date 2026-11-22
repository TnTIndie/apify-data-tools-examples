// DNS Records Lookup: MX, SPF, DMARC, A, TXT ($0.5/1K)
// DNS records lookup: A, AAAA, CNAME, MX, NS, TXT, SOA and CAA records, plus mail provider, SPF record and DMARC policy. Takes a list of domains and queries public DNS over HTTPS. Use it to check MX records and email deliverability setup (SPF, DMARC) for many domains.
// Apify page: https://apify.com/tamnt67/dns-records-lookup
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "domains": [
        "apify.com",
        "github.com",
        "stripe.com",
        "shopify.com",
        "proton.me"
    ],
    "checkEmailSecurity": true
};

const run = await client.actor('tamnt67/dns-records-lookup').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
