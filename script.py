import json
from prettytable import PrettyTable

f = open("request.json")

data = json.load(f)

print("Welcome to the EUR currency converter!")

run = True

def new_consult():
    global run
    option = int(input("Do you want to calculate another value? yes(1) no(2) "))
    if option == 1:
        run = True 
    else:
        run = False

while run:
    table = PrettyTable()
    table.field_names = ["Amount", "Base currency","Currency chosen", "Total"]

    base_currency = input("Type the base currency(Ex: BRL, USD): ").upper()
    currency = input("Type the currency you want to convert(Ex: BRL, USD): ").upper()
    convert = float(input("Type the value to be converted: "))

    base = data["base"]

    converted = round(convert * (data["rates"][currency]/data["rates"][base_currency]), 2)

    table.add_row([convert, base_currency, currency, converted])

    print(table)
    new_consult()

