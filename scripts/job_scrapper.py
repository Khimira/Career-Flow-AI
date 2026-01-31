import json
import sys
import argparse
from jobspy import scrape_jobs

def fetch_jobs(term, location, results):
    """
    Fetches recent job postings using JobSpy and returns them as a JSON string.
    """
    try:
        jobs = scrape_jobs(
            site_name=['linkedin'],
            search_term=term,
            location=location,
            results_wanted=results,
            hours_old=24,
            country_indeed='brazil' 
        )
        
        # Convert DataFrame to JSON and print to stdout
        print(jobs.to_json(orient='records'))

    except Exception as e:
        # Structured error handling for n8n to parse
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Career-Flow AI: Job Scraper')
    parser.add_argument('--term', type=str, default='DevOps', help='Job title to search')
    parser.add_argument('--loc', type=str, default='Brazil', help='Location')
    parser.add_argument('--limit', type=int, default=5, help='Number of results')

    args = parser.parse_args()
    fetch_jobs(args.term, args.loc, args.limit)
