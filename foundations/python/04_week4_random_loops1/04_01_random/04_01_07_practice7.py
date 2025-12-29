import random
a=[1,2,3,4,5]
n1=int(input('n1: '))
n2=int(input('n2: '))
print(random.randrange(n1,n2))
random.shuffle(a)
print('a:',a)
print(random.choice(a))
print()
