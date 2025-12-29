# Calculate bill counts using the input function

money = int(input("Enter the amount to be exchanged: "))

m_50000 = money//50000; money_changes = money%50000
m_10000 = money_changes//10000; money_changes = money%10000
m_5000 = money_changes//5000; money_changes = money%5000
m_1000 = money_changes//1000; money_changes = money%1000

print("50,000-won bills: %d" %m_50000)
print("10,000-won bills: %d" %m_10000)
print("5,000-won bills: %d" %m_5000)
print("1,000-won bills: %d" %m_1000)
print("Remaining amount after exchanging bills: %d won" %money_changes)
