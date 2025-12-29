print('''Throw a red die and a blue die.
If their total is greater than 9, you become a millionaire;
otherwise, you end up broke.
What will your fate be? You only have 3 chances.''')


import random

game = 3

while game:
    input("Press Enter to start the game.")
    
    red = random.randint(1, 6)
    blue = random.randint(1, 6)
    total = red + blue
    
    print(f"Red: {red}, Blue: {blue}, Total: {total}")
    
    if total > 9:
        print("You've become a millionaire!")
        break
    else:
        print("Looks like you're going to be broke…")

    game = game-1

    print(f"You have {game} attempts left.")
    
    if game == 0:
        print("Ahhh… You’ve gone broke.")
