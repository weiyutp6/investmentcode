import alpaca_trade_api as tradeapi
import pandas as pd
import yaml

# Initialize the REST API client with your Alpaca API credentials
api = tradeapi.REST('AKM3OXUHD88ULTYYX4JD', 'vwYdV1KD63FIaYqZwhpFdlwOP7tNIGYzp4y23JgS', base_url='https://paper-api.alpaca.markets')

# Load stock symbols from the YAML file
with open('stock_symbols.yaml', 'r') as file:
    stocks_data = yaml.safe_load(file)

# Define the date range for fetching historical data
start_date = '2022-09-01'
end_date = '2022-09-07'

def get_stock_data(symbol, start_date, end_date):
    """Fetch historical data for a given stock symbol."""
    bars = api.get_bars(symbol, tradeapi.TimeFrame.Day, start_date, end_date).df
    return bars

# Fetch and print historical data for each stock symbol
if __name__ == "__main__":
    for stock in stocks_data['stocks']:
        symbol = stock['symbol']
        stock_data = get_stock_data(symbol, start_date, end_date)
        print(f"Historical data for {symbol} ({stock['name']}):")
        print(stock_data)
        print("\n")
