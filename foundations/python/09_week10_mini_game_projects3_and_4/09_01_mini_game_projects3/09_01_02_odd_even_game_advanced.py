import random

print("The odd-or-even game is starting. The game will be played 3 times.")

game = 3
win = 0
lose = 0

while(game):
    number = random.randint(1,100)

    while(True):
        your_num = input("Enter an integer:")

        if not your_num.isnumeric():
            print("It is not an integer.")
            continue
        break
    
    game = game-1
    
    your_num2 = int(your_num)
    
    if(number%2 == your_num2%2):
        print("You win!")
        win = win+1
    else:
        print("You lose.")
        lose = lose+1

    print(f"Generated random integer: {number}")
    print(f"Win: {win}, Lose:{lose}")
