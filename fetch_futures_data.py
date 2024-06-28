import os
import requests
import pandas as pd
import yaml

API_KEY = os.getenv('QUANDL_API_KEY', 'a7T-9ZaMG1vAQysJPHn4')  # Replace this with your Quandl API key or set it as an environment variable
DATA_DIR = 'data'
CSV_FILE_PATH = os.path.join(DATA_DIR, 'futures_data.csv')
YAML_FILE_PATH = 'futures_codes.yaml'

def load_futures_codes(yaml_file):
    with open(yaml_file, 'r') as file:
        futures_codes = yaml.safe_load(file)
    return futures_codes

def get_futures_data(futures_code):
    url = f'https://www.quandl.com/api/v3/datasets/{futures_code}.json?api_key={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return

    if 'dataset' in data:
        df = pd.DataFrame(data['dataset']['data'], columns=data['dataset']['column_names'])

        print(df)
    else:
        print(f"Error: {data}")

if __name__ == "__main__":
    futures_codes = load_futures_codes(YAML_FILE_PATH)

    # Example: Fetch data for Crude Oil (WTI) futures
    example_code = futures_codes['futures_codes']['commodities'][0]['code']
    get_futures_data(example_code)
