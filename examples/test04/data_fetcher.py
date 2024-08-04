import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_gold_price_data():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": "API-KEY"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

    data = response.json()

    # If 'date' is not in the response, use the current timestamp
    if 'date' not in data:
        data['date'] = datetime.now().isoformat()

    df = pd.DataFrame([data])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    return df
