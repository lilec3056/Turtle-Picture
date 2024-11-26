import turtle              # allows us to use the turtles library
from turtle import *

wn = turtle.Screen()        # creates a graphics window

# Turtles

theodore = turtle.Turtle()      # create a turtle named theodore
theodore.color('Coral')

donald = turtle.Turtle()        # create a turtle named donald
donald.color('DarkBlue')


def draw_shape(num_sides):
    angle = 180 - (((num_sides - 2) * 180) / num_sides)
    repeat = 0

    theodore.begin_fill()
    while repeat != num_sides:

        theodore.forward(50)
        theodore.left(angle)
        repeat += 1
    theodore.end_fill()


number_of_sides = int(input("Number of sides: "))
draw_shape(number_of_sides)

donald.forward(300)







# program ends without closing window.
turtle.done()
