# practice 5

print('Numbers from 1 to 10 are listed. Try to find the number Yeona likes within 5 attempts.')
start = 1
end = 10
val = 3  # the number Yeona likes
trial = 1

while trial <= 5:
    num = int(input('num: '))

    if num < start or num > end:
        print('Please enter a number between 1 and 10.')
        continue

    if num < val:
        print('Guess a bigger number')
    elif num > val:
        print('Guess a smaller number')
    else:
        print('Correct!')
        break

    trial = trial + 1

print('The number Yeona likes is', val)
