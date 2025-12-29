# Mini Project 1 - Basic Arithmetic & Capital City Quiz Game

def explain_game():
    print('''----------- game -----------
This program is the first game created.
Press 1 to try basic arithmetic.
Press 2 to start the country–capital matching game.''')

def ns():
    a=int(input('val1: '))
    b=int(input('val2: '))
    print('a+b=',a+b, ' a-b=',a-b,' a*b=', a*b, ' a/b=',a/b)


def nm():
    print('What is the capital of Korea?')
    ans = input()
    if ans == 'Seoul':
        print('Correct!')
    else:
        print('Wrong answer.')


def sel_2(n):
    if n==1:
        ns()
    elif n==2:
        nm()
    else:
        print('Please press 1 or 2.')


explain_game()
select=int(input('select(1~2):'))
sel_2(select)
