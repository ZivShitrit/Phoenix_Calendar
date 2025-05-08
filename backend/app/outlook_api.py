import requests
from msal import ConfidentialClientApplication
import os
from dotenv import load_dotenv
from pathlib import Path

# Finds Path to this file's Location for .env file load
BASE_DIR = Path(__file__).resolve().parent
dotenv_path = BASE_DIR / ".env"

load_dotenv(dotenv_path)

def get_calendar_data():
    # Application details from azure
    CLIENT_ID = os.getenv("CLIENT_ID")
    TENANT_ID = os.getenv("TENANT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    USER_EMAIL = os.getenv("EMAIL")

    # Application Settings 
    authority = f"https://login.microsoftonline.com/{TENANT_ID}"
    app = ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=authority
    )

    # Token Request
    scope = ["https://graph.microsoft.com/.default"]
    result = app.acquire_token_for_client(scopes=scope)

    if "access_token" in result:
        access_token = result["access_token"]

        # Get User's Calendar Events
        endpoint = f"https://graph.microsoft.com/v1.0/users/{USER_EMAIL}/calendar/events"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            events = response.json().get("value", [])
            return events
        else:
            return "Error Reading Calendar: " + response.status_code, response.text
    else:
        return "Error Getting Token:" + result.get("error_description")
