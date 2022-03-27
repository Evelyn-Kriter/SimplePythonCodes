#Evey Kriter CSCI 0101 this assignment is for practicing recursion

import turtle

def draw_sierpinski(length, iterations):            
    '''Here's the code that actually draws the sierpinski'''
    if iterations == 0:
        turtle.left(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length/2)
        turtle.right(60)
        turtle.forward(length/2)
        turtle.right(120)
        turtle.forward(length/2)
        turtle.right(120)
        turtle.forward(length/2)
        turtle.right(60)
        turtle.forward(length/2)
        turtle.right(180)
    elif iterations > 0:
        draw_sierpinski(length/2, iterations-1)
        turtle.up()
        turtle.forward(length/2)
        turtle.down()
        draw_sierpinski(length/2, iterations-1)
        turtle.up()
        turtle.backward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        turtle.down()
        draw_sierpinski(length/2, iterations-1)
        turtle.up()
        turtle.right(120)
        turtle.forward(length/2)
        turtle.left(120)
        turtle.down()
    turtle.update
    turtle.done

def draw_scene():
    """
    Use this code to call your sierpinski_triangle() function. This provides
    the functionality of turning off the tracer and stopping the turtle so
    you don't need to worry about it.
    """
    # this means we don't have to wait for the turtle to draw the shape
    turtle.tracer(False)
    
    # pick up the pen and move the turtle so it starts at the left edge of the canvas
    turtle.up()
    turtle.goto(-turtle.window_width()/2 + 20, 0)
    turtle.down()
    
    # change the values in here for different sizes
    draw_sierpinski(600, 4)

draw_scene()