# mini project 1

import random

def opening():
    print('''========================================
Through this game,
your character and the monster can battle up to 5 times.
The final winner will be determined through these battles.
Both your character and the monster start with 50 energy.

During the total of 10 possible battles,
the battle power will change based on random energy values between -50 and +50.
If either side’s energy becomes less than 0, the game ends immediately.

If both still have more than 0 energy after 5 battles,
the one with the higher energy is declared the winner.
========================================''')

def character_choice():
    print('''Choose your character (1–3)
1) Bear
2) Cat
3) Puppy''')
    a=int(input())
    return a

def battle(a):
    a_e = 50
    mon_e = 50
    for i in range(5):
        a_e = a_e + random.randint(-50, 50)
        mon_e = mon_e + random.randint(-50, 50)
        print(i+1, "round,", a, "'s energy is", a_e, "and the monster's energy is", mon_e)

        if a_e < 0 and mon_e > 0:
            print("Monster wins!!!")
            break
        elif a_e > 0 and mon_e < 0:
            print(a, "wins!!!")
            break
        else:
            print("Hmm… neither side is satisfied.")
            if i == 4:
                print("Both are declared winners!!!")
                break


opening()

while True:
    num = character_choice()

    if num == 1:
        battle('bear')
        break
    elif num == 2:
        battle('cat')
        break
    elif num == 3:
        battle('puppy')
        break
    else:
        print('Incorrect character. Please choose again.')





