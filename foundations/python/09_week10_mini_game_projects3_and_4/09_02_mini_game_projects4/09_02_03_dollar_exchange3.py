# User enters the amount to exchange (using input)

while (True):
    money = input("Enter the amount to exchange: ")

    if not money.isnumeric():
        print("It is not an integer.")
        continue
    break

money = int(money)

while (True):
    dollar = input("Enter the exchange rate: ")

    if not dollar.isnumeric():
        print("It is not an integer.")
        continue
    break

dollar = int(dollar)


dollar_100 = money // (dollar * 100)
money_return = money % (dollar * 100)

dollar_10 = money_return // (dollar * 10)
money_return = money_return % (dollar * 10)

dollar_5 = money_return // (dollar * 5)
money_return = money_return % (dollar * 5)

dollar_1 = money_return // dollar
money_return = money_return % dollar

print(f"{dollar_100} hundred-dollar bills.")
print(f"{dollar_10} ten-dollar bills.")
print(f"{dollar_5} five-dollar bills.")
print(f"{dollar_1} one-dollar bills.")
print(f"The remaining amount in KRW is {money_return} won.")
