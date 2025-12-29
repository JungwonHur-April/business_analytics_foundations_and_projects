import random
a=random.randint(1,20)
b=random.randint(1,20)
n=int(input('n:'))
if a>=b:
    val=random.sample(range(b,a+1),n)
elif b>a:
    val=random.sample(range(a,b+1),n)
print('a: ',a,'b: ',b)
print(val)
