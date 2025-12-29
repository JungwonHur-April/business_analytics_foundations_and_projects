import random

print("You must be a Hanyang Cyber University student.")
print("Please enter your name.")
name = input()
print()

realnum = random.randint(1, 5)
print("Hi", name + ",", "guess a random number (1~5).")

guessnum = 0

while realnum != guessnum:
    guessnum = input("Enter your number: ")
    guessnum = int(guessnum)

    if guessnum < realnum:
        print("Guess a bigger number.")
    if guessnum > realnum:
        print("Guess a smaller number.")
    if guessnum == realnum:
        print("Good job!", name + ".", "Have a nice day!")
