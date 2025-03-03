import csv

def load_exchange_rates(filename):
    """Load currency exchange rates from a CSV file into a dictionary."""
    exchange_rates = {}

    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            currency_code = row['code']
            exchange_rates[currency_code] = float(row['rate'])

    return exchange_rates

def convert_usd(amount, target_currency, exchange_rates):
    """Convert an amount in USD to a specified currency using exchange rates."""
    if target_currency in exchange_rates:
        return amount * exchange_rates[target_currency]
    else:
        print(f"Error: Exchange rate for {target_currency} is not available.")
        return None

def main():
    """Main function to gather user input and execute currency conversion."""
    filename = 'currency.csv'
    exchange_rates = load_exchange_rates(filename)

    try:
        usd_amount = float(input("Enter the amount in USD: "))
        target_currency = input("Enter the target currency code: ").strip().upper()

        converted_amount = convert_usd(usd_amount, target_currency, exchange_rates)

        if converted_amount is not None:
            print(f"{usd_amount} USD is equivalent to {converted_amount:.2f} {target_currency}.")
    except ValueError:
        print("Invalid input! Please provide a valid number for the USD amount.")

if __name__ == "__main__":
    main()