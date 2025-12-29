import random
a=int(input('a:'))
b=int(input('b:'))
if a<=b:
    print(random.randint(a,b))
else:
    print('error: a>b')
