#Evey Kriter/10.4.2019/CSCI0101/Lab4/This assignment is to teach us how to use random and to practice more recursion.

import turtle
import random

def draw_tree(length, generations):
    '''This function tells the turtle how to draw a tree'''
    length = length + random.randint(-length//10, length//10 + 1)
    turtle.width(length/15)
    if generations == 1:
        turtle.forward(length)
        turtle.backward(length)
    elif generations > 1:
        x = 30 + random.randint(-10, 10)
        y = 30 + random.randint(-10, 10)
        turtle.forward(length)
        turtle.left(x)
        draw_tree(length/1.5, generations-1)
        turtle.up()
        turtle.down()
        turtle.width(length/15)
        turtle.right(x)
        turtle.right(y)
        draw_tree(length/1.5, generations-1)
        turtle.up()
        turtle.down()
        turtle.left(y)
        turtle.up()
        turtle.backward(length)
        turtle.down()

def draw_scene():
    ''' This function moves the turtle down to the bottom of the screen and points it upward in preparation for drawing a tree.'''
    turtle.up()
    turtle.goto(0, -turtle.window_height()/2 +20)
    turtle.left(90)
    turtle.down()
    turtle.tracer(False)
    draw_tree(400,12)
    turtle.update()

    turtle.done()

draw_scene()