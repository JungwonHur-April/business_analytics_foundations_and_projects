import random
import time

dan = random.randint(2, 9)
print("dan:", dan)
print("Printing", dan)
time.sleep(1)

for i in range(1, 10):
    print(dan, "*", i, "=", dan * i)
print()
