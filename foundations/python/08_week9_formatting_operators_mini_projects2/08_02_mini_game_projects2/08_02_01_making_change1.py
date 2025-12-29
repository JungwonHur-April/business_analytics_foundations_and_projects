'''
Youngchul saved money in a piggy bank for a year and ended up with 187,652 won.
At the bank, he exchanged the money for 50,000-won, 10,000-won, 5,000-won, and 1,000-won bills.
How many bills of each denomination did he receive, and how much coin money was left over?
'''

money = 187652
m_50000 = money//50000
money_changes1 = money%50000

print("50,000-won bills: %d" %m_50000)
print("The remainder after removing the 50,000-won bills: %d won" %money_changes1)


m_10000 = money_changes1//10000
money_changes2 = money_changes1%10000

print("10,000-won bills: %d" %m_10000)
print("The remainder after removing the 10,000-won bills: %d won" %money_changes2)


m_5000 = money_changes2//5000
money_changes3 = money_changes2%5000

print("5,000-won bills: %d" %m_5000)
print("The remainder after removing the 5,000-won bills: %d won" %money_changes3)


m_1000 = money_changes3//1000
money_changes4 = money_changes3%1000

print("1,000-won bills: %d" %m_1000)
print("The remainder after removing the 1,000-won bills: %d won" %money_changes4)



