import random
number = random.randint(1,100)

if(number%2 == 0):
    print("even")
else:
    print("odd")

print(f"Generated random integer: {number}")  # f-string: Insert variables directly into a string using curly braces { }.
