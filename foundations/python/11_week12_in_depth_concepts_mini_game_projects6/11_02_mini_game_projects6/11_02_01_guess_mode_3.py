print(
    "The male robot chooses a number from 1 to 3.\n"
    "The female robot also chooses a number from 1 to 3.\n"
    "Then you choose a number, but you must avoid the number chosen by the female robot.\n\n"
    "Scoring Rules:\n"
    "- If the female robot guesses the male robot's number, she wins.\n"
    "  She gains 1 ball, and the male robot loses 1 ball.\n"
    "- If you guess the male robot's number, you win.\n"
    "  You gain 1 ball, and the male robot loses 1 ball.\n"
    "- If neither you nor the female robot guesses correctly, the male robot wins.\n"
    "  He gains 2 balls, while both you and the female robot lose 1 ball each.\n\n"
    "Everyone starts with 3 balls.\n"
    "If any player reaches 0 balls, the game ends immediately.\n"
    "The player with the most balls at the end becomes the final winner.\n\n"
    "Can you become the ultimate champion?"
)


import random

m_ball = 3
w_ball = 3
y_ball = 3

while not (m_ball == 0 or w_ball == 0 or y_ball == 0):
    m_robot = random.randint(0, 2)
    w_robot = random.randint(0, 2)

    print(f"The female robot chose {w_robot}.")
    print("What is your choice?")
    print("Choose 0, 1, or 2: ")
    
    while True:
        you = int(input())

        if you == w_robot:
            print("You cannot choose the same number as the female robot. Choose again.\n")
        else:
            break

    if m_robot == you:
        print("You win!")
        y_ball += 1
        m_ball -= 1
    
    elif m_robot == w_robot:
        print("The female robot wins!")
        w_ball += 1
        m_ball -= 1

    else:
        print("The male robot wins!")
        w_ball -= 1
        y_ball -= 1
        m_ball += 2

    print(f"Male robot chose: {m_robot}, Female robot chose: {w_robot}, You chose: {you}.")
    print(f"Balls remaining — Male robot: {m_ball}, Female robot: {w_ball}, You: {y_ball}")
    print("\n")

