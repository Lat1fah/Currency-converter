from requests import get 
from pprint import PrettyPrinter

BASE_URL = "https://api.frankfurter.dev"

printer = PrettyPrinter()

def get_currencies():
    endpoint = "/v1/currencies"  #so for frankfurter we use this and not =>  #f"api/v7/currencies?apiKey={API_KEY}" #I followed a tutorial for this, but frankfurter doesn't have an API key, so idk if this will work? If it doesn't we'll find a workaround. 
    url = BASE_URL + endpoint 
    data = get(url).json()            #this is a http request

    data = list(data.items()) #this is supposed to sort out all the currencies from different countries. 
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies: 
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")
        print(f"{_id}-{name}-{symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"/v1/currencies = {currency1}_{currency2}" 
    url = BASE_URL + endpoint
    data = get(url)

    data = response.json
    if len(data)==0:
        print("Invalid currencies.")

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try: 
        amount = float(amount)
    except:
        print("invalid amount.")
        return

    converted_amount = rate *amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()

    print("Welcome to the currency converter")
    print("List - lists the different currencies")
    print("Convert- convert from one currency to another")
    print("Rate - get the exchange rate")
    Print()

    while True:
        command = input ("Enter a command (press Q to quit)").lower()

        if command == "q":
            break 
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency id: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to id: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency id: ").upper()
            currency2 = input("Enter a currency to convert to id: ").upper()
            exchange_rate = (currency1, currency2)
        else:
            print("unrecognized command!")

main()


