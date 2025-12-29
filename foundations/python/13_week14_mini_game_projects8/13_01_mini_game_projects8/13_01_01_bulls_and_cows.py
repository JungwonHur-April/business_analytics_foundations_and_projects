import random

a = [0, 0, 0]
attempts = 0

while (a[0] == a[1] or a[0] == a[2] or a[2] == a[1]):
    a = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]

print(str(a[0]) + str(a[1]) + str(a[2]))  # for checking

while True:
    strike = 0
    ball = 0
    number_ok = True
    is_ok = False

    while is_ok == False:
        b = input("Enter a 3-digit number with all different digits: ")

        if len(b) != 3:
            print("This is not a 3-digit number.")
            number_ok = False
            break

        for i in range(3):
            if (b[i] < '0' or b[i] > '9'):
                print("This is not a numeric value.")
                number_ok = False
                break

        if number_ok == False:
            break

        if (b[0] == b[1] or b[0] == b[2] or b[2] == b[1]):
            print("The digits are not all different.")
            number_ok = False
            break

        if number_ok == True:
            print(f"The entered 3-digit number with all different digits is {b}.")
            is_ok = True
            break

    if number_ok == False:
        continue

    for i in range(3):
        if a[i] == int(b[i]):
            strike = strike + 1

    for i in range(3):
        for j in range(3):
            if (int(b[j]) == a[i] and i != j):
                ball = ball + 1

    attempts = attempts + 1

    print(f"Strike: {strike}, Ball: {ball}")

    if (strike == 3):
        print("Correct!")
        print(f"You cleared it in {attempts} attempts!")
        break
