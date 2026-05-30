"""
Google Jobs API: A Quick Start Example
See more at: https://apify.com/johnvc/Google-Jobs-Scraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/Google-Jobs-Scraper/input-schema?fpr=9n7kx3

This script shows how to call the Google Jobs API on Apify from Python and read its
structured JSON output. It exercises several input parameters so you can see what
is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Billing is per page processed, so max_pagination is kept at 1 to keep this first
# run inexpensive. Raise it once you have your own API key and know your budget.
run_input = {
    "query": "Software Engineer",
    "location": "San Francisco, CA",
    "country": "us",                 # country code
    "language": "en",                # language code
    "num_results": 10,               # cap on results
    "max_pagination": 1,             # pages to fetch; kept at 1 to stay cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/Google-Jobs-Scraper").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset (one item per job listing)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} job(s).\n")

# Show a few key fields from each job.
for item in items[:10]:
    apply_link = ""
    options = item.get("apply_options") or []
    if options:
        apply_link = options[0].get("link", "")
    print(f"{item.get('title')}  |  {item.get('company_name')}  |  {item.get('location')}  [{item.get('via')}]")
    if apply_link:
        print(f"   apply: {apply_link}")
