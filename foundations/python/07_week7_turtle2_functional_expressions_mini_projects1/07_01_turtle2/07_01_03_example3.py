# example 3

import turtle as t
screen = t.getscreen()
turtle = t.Turtle()
def move_forward():
    turtle.left(10) # Even with turtle as t, turtle still works.
    turtle.forward(50)

screen.listen()
screen.onkey(move_forward,"Up")
screen.mainloop()
