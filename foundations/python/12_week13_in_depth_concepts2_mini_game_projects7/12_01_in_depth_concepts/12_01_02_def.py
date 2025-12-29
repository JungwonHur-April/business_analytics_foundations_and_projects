import random

game = 5

options = ["Scissors", "Rock", "Paper"]

def get_computer_choice():
    return random.choice(options)

while game:
    computer_choice = get_computer_choice()
    print(f"Computer's choice: {computer_choice}")
    game -= 1
