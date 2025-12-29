a = 3
b = 5

print(f"The result of a == 5 and b == 5 is {a == 5 and b == 5}")
print(f"The result of a == 5 or b == 5 is {a == 5 or b == 5}")
print(f"The result of not(a == 5 or b == 5) is {not(a == 5 or b == 5)}")


c = 3
d = 5

while(not(c == 10 or d == 10)):
    print(f"c = {c} d = {d}")
    c = c+1
    d = d+1
