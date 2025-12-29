# format specifier

# %s
temp_string = "Hanyang Cyber University"
print("%s" % temp_string)

# %d
money = 318765
m_50000 = money  // 50000
print("50,000-won bills: %d" % m_50000)

# %f
m_50000 = money / 50000
print("50,000-won bills (float): %f" % m_50000)

# %d vs %f
m_50000 = money % 50000
print("Remaining amount: %f" % m_50000)
print("Remaining amount: %d" % m_50000)
