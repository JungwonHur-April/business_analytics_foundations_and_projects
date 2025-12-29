import random
count=0
for i in range(5):
    score=random.randint(0,100)
    print(score,end=' ')
    if score>=90:
        count=count+1
print('The number of students with score over 90: ',count)
