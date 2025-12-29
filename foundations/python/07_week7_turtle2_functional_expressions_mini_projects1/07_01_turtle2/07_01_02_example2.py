# example 2

import turtle as t

def left():
    t.setheading(180)
    t.forward(100)

def right():
    t.setheading(0)
    t.forward(100)
    
def forwd():
    t.setheading(90)
    t.forward(100)

def backwd():
    t.setheading(270)
    t.forward(100)

screen = t.getscreen()

screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")
screen.onkeypress(forwd,"Up")
screen.onkeypress(backwd,"Down")

screen.listen()
