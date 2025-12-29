print("Print a multiplication table (odd-numbered tables only).")
print("If an invalid table (not 2~9) is chosen, the program ends.\nChoose a table.")

while True:
    dan = int(input("dan: "))
    if dan < 2 or dan > 9:
        print("Invalid table.")
        break
    if dan % 2 == 0:
        print("This is an even-numbered table.")
        continue
    for i in range(1, 10):
        print(dan, "*", i, "=", dan * i)
print()
