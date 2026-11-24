// FDA Drug Safety & Clinical Trials Scraper ($3/1K)
// FDA and ClinicalTrials.gov scraper: trials with sponsor, phase, status, enrollment, eligibility, sites; FDA drug labels, FAERS adverse events, recalls and label interaction checks. Takes drug names, conditions, filters, NCT IDs or a search URL. Use it to track pharma pipelines and drug safety.
// Apify page: https://apify.com/tamnt67/fda-clinical-trials-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "mode": "trials_search",
    "condition": "obesity",
    "limit": 50
};

const run = await client.actor('tamnt67/fda-clinical-trials-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
