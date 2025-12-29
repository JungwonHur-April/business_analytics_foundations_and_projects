import random
min=101
max=39
for i in range(5):
    score=random.randint(40,100)
    print(score,end=' ')
    if score>max:
        max=score
    elif score<min:
        min=score
print('min= ',min,' max= ',max)
print()
