import random

game = 5
win = 0
lose = 0
draw = 0

options = ["Scissors", "Rock", "Paper"]

def get_computer_choice():
    return random.choice(options)

def get_user_choice():
    user_input = input("Choose one: Scissors, Rock, or Paper: ")

    while user_input not in options:
        user_input = input(
            "Invalid input. Please enter exactly one of: Scissors, Rock, or Paper: "
        )

    return user_input

def determine_winner(user_choice, computer_choice):
    global win
    global lose
    global draw

    if user_choice == computer_choice:
        draw += 1
        return "It's a draw!"
    elif (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        win += 1
        return "Congratulations! You win!"
    else:
        lose += 1
        return "Unfortunately, the computer wins."

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Computer's choice: {computer_choice}")
    print(f"Your choice: {user_choice}")
    print(determine_winner(user_choice, computer_choice))
    print(f"Record: {win} Wins, {draw} Draws, {lose} Losses")

while win < 2 and lose < 2:
    play_game()
