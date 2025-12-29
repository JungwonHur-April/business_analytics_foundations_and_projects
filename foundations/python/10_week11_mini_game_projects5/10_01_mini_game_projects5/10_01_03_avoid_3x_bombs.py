print('''Move forward by the number shown on the die you roll.
Traps are placed on multiples of 3.
Can you safely pass 19 and rescue the princess?''')

import random

total = 0
game = 1

while game:
    input("Press Enter to start the game.")
    
    red = random.randint(1, 6)
    total = total + red
    
    print(f"Red: {red}, Total: {total}")
    
    if total % 3 == 0:
        print("it's a bomb!")
        game = 0

    if total > 19:
        print("Mission accomplished!!!")
        break
