'''
Sue is traveling to the United States with her friends.
The exchange rate shows that 1 dollar equals 1,475 won.
With one million won, how many 100-dollar bills can she receive?
And how much money will she get back?
'''

money = 1000000
dollar = 1475

dollar_100 = money // (dollar * 100)
money_return = money % (dollar * 100)

print(f"{dollar_100} pieces of 100-dollar bills can be received.")
print(f"The remaining amount in KRW is {money_return} won.")
print(f"1 dollar equals {dollar} won.")
