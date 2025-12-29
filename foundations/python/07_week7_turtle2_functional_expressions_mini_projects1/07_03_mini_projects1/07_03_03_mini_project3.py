# Mini Project 3 - Catch the Heart!

import random

def heart():
    import turtle as t
    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Generate five winning numbers (0~10)
lucky_num1 = random.randint(0, 10)
lucky_num2 = random.randint(0, 10)
lucky_num3 = random.randint(0, 10)
lucky_num4 = random.randint(0, 10)
lucky_num5 = random.randint(0, 10)

print("This week's lucky card numbers have been set. Matching even one number earns you a heart.")

print("Enter your lucky numbers (five numbers between 0 and 10, separated by spaces): ")
user_num1, user_num2, user_num3, user_num4, user_num5 = map(int, input().split())

match_count = 0
match_count += lucky_num1 in [user_num1, user_num2, user_num3, user_num4, user_num5]
match_count += lucky_num2 in [user_num1, user_num2, user_num3, user_num4, user_num5]
match_count += lucky_num3 in [user_num1, user_num2, user_num3, user_num4, user_num5]
match_count += lucky_num4 in [user_num1, user_num2, user_num3, user_num4, user_num5]
match_count += lucky_num5 in [user_num1, user_num2, user_num3, user_num4, user_num5]

if match_count >= 1:
    print("Congratulations! Here's a heart for you!")
    heart()
else:
    print("Unfortunately, try again next time!")

print("This week's lucky numbers are:")
print(lucky_num1, lucky_num2, lucky_num3, lucky_num4, lucky_num5)
