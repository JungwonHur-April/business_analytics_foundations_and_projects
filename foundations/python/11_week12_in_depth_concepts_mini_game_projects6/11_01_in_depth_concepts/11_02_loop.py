# 1
for i in range(0, 3):
    print(f"{i} push-up")
    print(f"{i} push-down")


# 2
print("\n")

total = 0
for i in range(1, 11):
    total = total + i
    print(f"Result of adding from 1 to {i}: {total}")


# 3
print("\n")

total = 0
for i in range(1, 5):
    total = total + i
print(f"Result of adding from 1 to {i}: {total}")
 

# 4
print("\n")

acc = 0
number = int(input("Enter a positive integer to sum up from 1: "))

for i in range(1, number + 1):
    acc = acc + i
    print(f"The result of adding from 1 to {i} is: {acc}")


# 5
print("\n")

print("Please select a menu option.")


while True:
    choice = int(input("1. Coke  2. Sparkling Water  3. Energy Drink: "))

    if choice == 1:
        print("You selected Coke.")
        break
    elif choice == 2:
        print("You selected Sparkling Water.")
        break
    elif choice == 3:
        print("You selected Energy Drink.")
        break
    else:
        print("Invalid selection.")




