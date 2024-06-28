# fetch_currency_data.py
import requests
import pandas as pd
import yaml

# Load configuration from YAML file
with open('currency_pairs.yaml', 'r') as file:
    config = yaml.safe_load(file)

CURRENCY_PAIRS = config['currency_pairs']
API_KEY = config['api_key']

def get_currency_data(currency_pair):
    API_URL = f'https://api-fxtrade.oanda.com/v3/instruments/{currency_pair}/candles'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'count': 100,
        'granularity': 'M1'  # 1-minute granularity for low latency
    }
    response = requests.get(API_URL, headers=headers, params=params)
    data = response.json()
    df = pd.DataFrame(data['candles'])
    print(f"Data for {currency_pair}:")
    print(df)
    return df

if __name__ == "__main__":
    all_data = {}
    df = get_currency_data("USD_TWD")
    # for pair in CURRENCY_PAIRS:
    #     print(pair)
    #     df = get_currency_data(pair)
    #     all_data[pair] = df
