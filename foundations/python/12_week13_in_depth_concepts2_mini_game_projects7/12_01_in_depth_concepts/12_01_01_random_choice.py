#1
import random

game = 5

while game:
    options = ["Scissors", "Rock", "Paper"]
    computer_choice = random.choice(options)

    print(f"Computer's choice: {computer_choice}")
    game -= 1



# 2
print("\n")
game2 = 1

while game2:
    options2 = ["Scissors", "Rock", "Paper"]

    print(f"Computer's choice: {options2[0]}")
    print(f"Computer's choice: {options2[1]}")
    print(f"Computer's choice: {options2[2]}")

    game2 -= 1
