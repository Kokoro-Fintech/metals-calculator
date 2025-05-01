# Purpose: import current values for gold, silver, and platinum

import requests
import sys

# Import decrypted api from Keychain - can be substituted for alternative methods to hard coding
sys.path.append('/path/to/decrypted/api') # Path where the decryption module is stored
from oanda_demo_api import get_decrypted_api_key

# OANDA API credentials
API_KEY = get_decrypted_api_key()  # Get the decrypted Personal Access Token (API key)
ACCOUNT_ID = 'your-account-id'  # Replace with your actual account ID
URL = f'https://api-fxpractice.oanda.com/v3/accounts/{ACCOUNT_ID}/pricing' # fxtrade = live / fxpractice = demo

# Parameters to get the prices of gold (XAU/USD), silver (XAG/USD), and platinum (XPT/USD)
params = {
    'instruments': 'XAU_USD,XAG_USD,XPT_USD'  # We request prices for gold, silver, and platinum
}

# Set up headers with the API key in the Bearer token format
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Function to get the live prices of gold, silver, and platinum
def get_prices():
    response = requests.get(URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            # Retrieve the bid prices of gold, silver, and platinum in USD per ounce
            gold_price_per_ounce = float(data['prices'][0]['bids'][0]['price'])
            silver_price_per_ounce = float(data['prices'][1]['bids'][0]['price'])
            platinum_price_per_ounce = float(data['prices'][2]['bids'][0]['price'])

            print(f"Live Gold Price: {gold_price_per_ounce} USD per ounce")
            print(f"Live Silver Price: {silver_price_per_ounce} USD per ounce")
            print(f"Live Platinum Price: {platinum_price_per_ounce} USD per ounce")
            return gold_price_per_ounce, silver_price_per_ounce, platinum_price_per_ounce
        except (KeyError, IndexError):
            print(f"Unexpected response format: {data}")
            return None, None, None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None, None, None