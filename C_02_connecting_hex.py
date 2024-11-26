import turtle              # allows us to use the turtles library
from turtle import *

import math
from math import *


john = turtle.Turtle()      # create a turtle named John
# john.color('DarkGoldenrod1')


def draw_shape(num_sides, direction):
    """Draws a polygon with a specified number of sides, direction is left / right"""
    angle = 180 - (((num_sides - 2) * 180) / num_sides)



    for item in range(num_sides):

        john.forward(50)
        if direction == left:
            john.left(angle)
            print("L")
        else:
            john.right(angle)
            print("R")

    print("done")




john.color('DarkGoldenrod1')
draw_shape(6, left)
john.right(120)
john.color('Red')
draw_shape(6, right)
# john.goto(50, 0)
# john.setheading(60)


john.color('Blue')
draw_shape(6, left)
john.setheading(0)
john.color('Green')
john.forward(50)
john.setheading(60)
draw_shape(6, right)

# program ends without closing window.
turtle.done()
