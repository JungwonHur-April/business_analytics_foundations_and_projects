import time
print("How many seconds should the program delay while printing numbers? (prints 1~5)")
n = int(input("seconds: "))

for i in range(5):
    print(i + 1)
    time.sleep(n)
print()
