# practice 3

def add(a,b):
    print(a,'+',b,'=',a+b)

def sub(a,b):
    print(a,'-',b,'=',a-b)

def mul(a,b):
    print(a,'*',b,'=',a*b)

def div(a,b):
    if b==0:
        print('error')
    else:
        print(a,'/',b,'=',a/b)

a=int(input('a:'))
b=int(input('b:'))

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
