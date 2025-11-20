import requests
import json
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scope for the Business Profile API
SCOPES = ['https://www.googleapis.com/auth/business.manage']

# File path to your OAuth 2.0 credentials.json
CREDENTIALS_FILE = 'credentials.json'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def authenticate():
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost:56009/flowName=GeneralOAuthFlow"] #"http://localhost"]
            }
        },
        SCOPES
    )
    creds = flow.run_local_server(port=0)
    return creds

def list_locations(creds):
    """List business locations."""
    headers = {"Authorization": f"Bearer {creds.token}"}
    url = "https://mybusinessbusinessinformation.googleapis.com/v1/locations"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def list_reviews(creds, location_name):
    """List reviews for a specific location."""
    headers = {"Authorization": f"Bearer {creds.token}"}
    url = f"https://mybusiness.googleapis.com/v4/{location_name}/reviews"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def reply_to_review(creds, location_name, review_id, reply_text):
    """Post a reply to a specific review."""
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json"
    }
    url = f"https://mybusiness.googleapis.com/v4/{location_name}/reviews/{review_id}/reply"
    payload = {
        "comment": reply_text
    }
    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    creds = authenticate()

    print("\nFetching locations...")
    locations = list_locations(creds)
    for loc in locations.get('locations', []):
        print(f"- {loc['name']} ({loc.get('title')})")

    # Pick a location manually or grab the first one
    location_name = locations['locations'][0]['name']
    print(f"\nUsing location: {location_name}")

    print("\nFetching reviews...")
    reviews = list_reviews(creds, location_name)
    for review in reviews.get('reviews', []):
        print(f"\nReview ID: {review['reviewId']}")
        print(f"Reviewer: {review['reviewer'].get('displayName')}")
        print(f"Comment: {review.get('comment')}")
        print(f"Star Rating: {review.get('starRating')}")

    # Pick a review ID to reply to
    if reviews.get('reviews'):
        review_id = reviews['reviews'][0]['reviewId']
        reply_text = "Thanks for your feedback! We appreciate it."

        print(f"\nReplying to review {review_id}...")
        # reply_result = reply_to_review(creds, location_name, review_id, reply_text)
        # print("Reply posted:", reply_result)
    else:
        print("No reviews found to reply to.")
