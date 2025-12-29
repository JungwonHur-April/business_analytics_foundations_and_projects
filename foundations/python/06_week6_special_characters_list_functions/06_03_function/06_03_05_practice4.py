# practice 4

#4-1
def studentinfo(n):
    for i in range(n):
        print(i+1,'th\'s student name is',"None")
        print(i+1,'\'s grade is ',"None")

studentinfo(3)

#4-2
def circle_area(n):
    return n*n*3.14

n=float(input('radius:'))
print(circle_area(n))
