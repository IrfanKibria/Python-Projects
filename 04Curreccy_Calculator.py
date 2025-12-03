# Write a function problem USD and BDT converter

def convert_currency():
    try: 
        currency = int(input("Enter which operation you want: press 1 for USD to BDT, press 2 for BDT to USD, 3 for Exit: "))
        if currency == 1:
            print("USD to BDT")
            return currency
        elif currency == 2:
            print("BDT to USD")
            return currency       
        elif currency == 3:
            print("Thank you for using calculator")
            return currency       
        else:
            print("Enter correct value between 1,2,3")
            return None
    except ValueError:
        print("Select correct value or valid input")
        return None



def currency_value():
    amount = float(input("Enter the Amount: "))
    return amount


def rate():
    usd = float(input("Enter USD Rate"))
    bdt = float(input("Enter BDT Rate"))
    return usd, bdt

def currency_calculator():
    while True:
        op = convert_currency()

        if op == None:
            continue

        if op == 3:
            break

        val = currency_value()
        a,b = rate()



        if op == 1:
            print("USD to BDT")
            result = val * a
            print(f"{val} USD = {result} Taka")

        elif op == 2:
            print("BDT to USD")
            result = val * b
            print(f"{val} Taka = {result} USD")

currency_calculator()
