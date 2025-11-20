import requests
from google_auth_oauthlib.flow import InstalledAppFlow

# Your Google Cloud OAuth 2.0 client ID and secret
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

SCOPES = ['https://www.googleapis.com/auth/business.manage']

def authenticate():
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
            }
        },
        SCOPES
    )
    creds = flow.run_local_server(port=56128)
    return creds

def list_locations(creds):
    headers = {"Authorization": f"Bearer {creds.token}"}
    url = "https://mybusinessbusinessinformation.googleapis.com/v1/locations"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    creds = authenticate()
    locations = list_locations(creds)
    print(locations)