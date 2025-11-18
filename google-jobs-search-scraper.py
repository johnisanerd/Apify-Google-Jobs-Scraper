"""
Google Jobs Search Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/apify-google-jobs?fpr=9n7kx3

This script demonstrates how to use the Google Jobs Search Scraper Actor
to search Google Jobs and retrieve structured search results.

https://docs.apify.com/api/client/python/docs/overview/introduction


"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient
from pprint import pprint

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "query": "Software Engineer",
    "location": "San Francisco, CA",
    "country": "us",
    "language": "en",
    "google_domain": "google.com",
    "num_results": 10,
    "max_pagination": 1,
    "include_lrad": False,
    "lrad_value": "5",
    "max_delay": 1,
    "output_file": "google_jobs_results.json",
}

print(f"Run the Aactor with Pay-Per-Event Pricing:  ")

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-jobs-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    pprint(item)


print(f"Run the Aactor with Pay-Per-Result Pricing:  ")

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-jobs-scraper---pay-per-result").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    pprint(item)