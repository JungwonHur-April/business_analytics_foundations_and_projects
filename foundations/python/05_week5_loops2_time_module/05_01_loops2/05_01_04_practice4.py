sum = 0
for i in range(0, 100):
    if i % 3 == 0:
        continue
    sum = sum + i
print("sum:", sum)
