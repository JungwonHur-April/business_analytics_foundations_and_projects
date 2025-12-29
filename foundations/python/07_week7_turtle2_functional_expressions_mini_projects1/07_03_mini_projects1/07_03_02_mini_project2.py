# Mini Project 2 - A Lucky Chance to Win 100 Million

import random

def start():
    print('''----------------- Game Description ------------------
You happened to pick up a set of cards.
You can write a total of 6 numbers on your cards.
If 2 or more of your numbers match the winning numbers,
you will receive a prize of 100 million.

Enter six numbers between 0 and 10 and try your luck!''')

def create_num():
    num =[]
    for i in range(6):
        a = random.randint(0,10)
        num.append(a)
    return num

yours = []
start()
my = []

for i in range(6):
    a = int(input('Enter a number between 0 and 10: '))
    my.append(a)

yours = create_num()
print('Winning numbers:', yours)

count = 0
for i in my:
    if i in yours:
        count = count+1

if count >= 2:
    print(count, 'numbers match. You won 100 million!')
