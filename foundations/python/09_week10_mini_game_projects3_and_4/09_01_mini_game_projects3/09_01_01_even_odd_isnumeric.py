import random
number = random.randint(1,100)

while(True):
    your_num = input("Enter an integer:")

    if not your_num.isnumeric():         # isnumeric(); Returns True if all characters in the given string are digits; otherwise, returns False.
        print("It is not an integer.")
        continue
    break

your_num2 = int(your_num)
if (number%2 == your_num2%2):
    print("You win!")
else:
    print("You lose.")
print(f"Generated random integer: {number}")
