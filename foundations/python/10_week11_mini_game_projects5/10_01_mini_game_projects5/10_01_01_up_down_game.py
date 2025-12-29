print('''Mia has been captured by an evil robot. Kevin must find the room number where she is being held.
The evil robot challenges Kevin to a duel—he only gets 5 chances.
Will Kevin be able to save Mia?
*How to play: Enter a number from 1 to 10 and the robot will give you a hint.''')


import random

game = 5
number = random.randint(1, 10)

while game:
    kevin = int(input("Enter an integer between 1 and 10: "))

    if number > kevin:
        print("The robot's number is higher than you.")
    elif number < kevin:
        print("Your number is higher than the robot.")
    else:
        print("Mission complete!!! Mia has been rescued!")
        break

    game = game-1
    print(f"{game} attempts left")
    
    if (game == 0):
        print("Game Over")
        break
