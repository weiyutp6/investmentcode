import requests
import pandas as pd
import yaml

API_KEY = 'a7T-9ZaMG1vAQysJPHn4'  # Replace this with your Quandl API key

def get_bond_codes():
    with open('bond_codes.yaml', 'r') as file:
        bond_codes = yaml.safe_load(file)
    return bond_codes['bonds']

def get_bond_data(bond_code):
    url = f'https://www.quandl.com/api/v3/datasets/{bond_code}.json?api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'dataset' in data:
        df = pd.DataFrame(data['dataset']['data'], columns=data['dataset']['column_names'])
        print(f"\nBond Data for {bond_code}:\n")
        print(df.head())  # Display only the first few rows for brevity
    else:
        print(f"Error fetching data for {bond_code}: {data}")

if __name__ == "__main__":
    bond_codes = get_bond_codes()
    get_bond_data(bond_codes[0]['code'])
