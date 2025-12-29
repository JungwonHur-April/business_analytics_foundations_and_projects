# Determine whether the computer-generated random integer is odd or even

import random

your_credit = 3
computer_credit = 3

while(your_credit > 0 and computer_credit > 0):
    computer_num = random.randint(1,100)
    your_num = int(input("Enter an integer: "))

    if(computer_num%2 == your_num%2):
        print("You win!")
        your_credit = your_credit+1
        computer_credit = computer_credit-1
    else:
        print("You lose.")
        your_credit = your_credit-1
        computer_credit = computer_credit+1

    print(f"Generated random integer: {computer_num}")
    print(f"Your credit is {your_credit}, and computer credit is {computer_credit}.")
