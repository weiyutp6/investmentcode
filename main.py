import importlib.util
import sys
from datetime import datetime

# Function to dynamically load a script
def load_script(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Load each script
fetch_bond_data = load_script('C:/Users/w7474/PycharmProjects/InvestmentCode/fetch_bond_data.py', 'fetch_bond_data')
fetch_currency_data = load_script('C:/Users/w7474/PycharmProjects/InvestmentCode/fetch_currency_data.py', 'fetch_currency_data')
fetch_futures_data = load_script('C:/Users/w7474/PycharmProjects/InvestmentCode/fetch_futures_data.py', 'fetch_futures_data')
fetch_options_data = load_script('C:/Users/w7474/PycharmProjects/InvestmentCode/fetch_options_data.py', 'fetch_options_data')
fetch_stock_data = load_script('C:/Users/w7474/PycharmProjects/InvestmentCode/fetch_stock_data.py', 'fetch_stock_data')

def get_user_input():
    code = input("Enter the code/symbol: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    return code, start_date, end_date

def main():
    while True:
        print("Select data type to fetch:")
        print("1. Stock")
        print("2. Bond")
        print("3. Futures")
        print("4. Options")
        print("5. Currency")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            code, start_date, end_date = get_user_input()
            data = fetch_stock_data.get_stock_data(code, start_date, end_date)
        elif choice == '2':
            code, start_date, end_date = get_user_input()
            data = fetch_bond_data.get_bond_data(code, start_date, end_date)
        elif choice == '3':
            code, start_date, end_date = get_user_input()
            data = fetch_futures_data.get_futures_data(code, start_date, end_date)
        elif choice == '4':
            code, start_date, end_date = get_user_input()
            data = fetch_options_data.get_options_data(code, start_date, end_date)
        elif choice == '5':
            code, start_date, end_date = get_user_input()
            data = fetch_currency_data.get_currency_data(code, start_date, end_date)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print("Fetched Data:", data)

if __name__ == "__main__":
    main()
