import random

game = 5
options = ["Scissors", "Rock", "Paper"]

def get_user_choice():
    user_input = input("Choose one: Scissors, Rock, or Paper: ")
    while user_input not in options:
        user_input = input(
            "Invalid input. Please enter exactly one of: Scissors, Rock, or Paper: "
        )
    return user_input

while game:
    user_choice = get_user_choice()
    print(f"Your choice: {user_choice}")
    game -= 1
