import requests
import pandas as pd
import yaml

# Polygon.io API endpoint for options data
API_URL = 'https://api.polygon.io/v3/reference/options/contracts'

# Replace with your Polygon.io API key
api_key = '8miSCT1rjPksKKp9zK_yGY3KmiYd1xuz'

# Load stock symbols from the YAML file
with open('stock_symbols.yaml', 'r') as file:
    stocks_data = yaml.safe_load(file)

# Function to fetch options data for a given stock symbol
def get_options_data(symbol):
    params = {
        'underlying_ticker': symbol,
        'apiKey': api_key
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data:
            options_df = pd.DataFrame(data['results'])
            return options_df
        else:
            print(f"No options data found for {symbol}")
            return pd.DataFrame()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return pd.DataFrame()

# Fetch and print options data for each stock symbol
if __name__ == "__main__":
    for stock in stocks_data['stocks']:
        symbol = stock['symbol']
        options_df = get_options_data(symbol)
        print(f"Options data for {symbol} ({stock['name']}):")
        print(options_df)
        print("\n")
