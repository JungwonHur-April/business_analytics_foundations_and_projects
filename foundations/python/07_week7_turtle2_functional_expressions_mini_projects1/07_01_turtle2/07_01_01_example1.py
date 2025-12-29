# example 1

import turtle

def a():
    turtle.left(30)
    turtle.fd(100)

s=turtle.getscreen()
turtle.onkeypress(a,"Up")
s.listen()
