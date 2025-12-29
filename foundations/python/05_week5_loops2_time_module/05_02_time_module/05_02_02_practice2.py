import time
a = time.time()
sum = 0
for i in range(0, 1000001):
    sum = sum + i
b = time.time()
print("sum:", sum)
print("time:", b - a)
