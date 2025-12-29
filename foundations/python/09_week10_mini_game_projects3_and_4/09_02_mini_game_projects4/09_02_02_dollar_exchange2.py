'''
Sue is traveling to the United States with her friends.
The exchange rate shows that 1 dollar equals 1,475 won.
With the remaining 83,200 won she received back,
how many 10-dollar, 5-dollar, and 1-dollar bills can she get?
And how much money will be left over?
'''

money = 83200
dollar = 1475

dollar_10 = money // (dollar*10)
money_return = money % (dollar*10)

dollar_5 = money_return // (dollar*5)
money_return = money_return % (dollar*5)

dollar_1 = money_return // dollar
money_return = money_return % dollar

print(f"{dollar_10} ten-dollar bills.")
print(f"{dollar_5} five-dollar bills.")
print(f"{dollar_1} one-dollar bills.")
print(f"The remaining amount in KRW is {money_return} won.")
