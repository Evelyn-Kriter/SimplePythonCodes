#Evey Kriter CSCI 0101 this assignment is for practicing recursion

import turtle

def spiral(initial_length, angle, multiplier):
    """
    This code tells python how to draw a spiral.
    """
    if 10000 > initial_length >= 1:
        turtle.forward(initial_length)
        turtle.right(angle)
        spiral((initial_length*multiplier), angle, multiplier)
    else:
        turtle.update
    
# this means we don't have to wait for the turtle to draw the shape
turtle.tracer(False)

# pick up the pen and move the turtle so it starts at the left edge of the canvas
turtle.up()
turtle.goto(-turtle.window_width()/2 + 20, 0)
turtle.down()

#Call the first spiral
turtle.pencolor("blue")
spiral(300, 90, 0.9)

# Move the turtle so it doesn't draw over what we have so far
turtle.up()
turtle.forward(200)
turtle.down()

# Call the second spiral
turtle.pencolor("green")
spiral(300, 92, 0.95)

turtle.done