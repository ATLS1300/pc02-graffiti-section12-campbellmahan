#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Campbell Mahan
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

turtle.up()
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.down()
turtle.color("dark orange")
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

turtle.color("black")
turtle.pensize(5)
turtle.left(90)
turtle.forward(140)
turtle.right(180)
turtle.forward(140)
turtle.left(90)

turtle.up()
turtle.left(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(250)
turtle.down()
turtle.color("dark grey")
turtle.begin_fill()
turtle.right(180)
turtle.forward(400)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(25)
turtle.end_fill()

turtle.up()
turtle.right(90)
turtle.forward(400)
turtle.left(90)
turtle.color("alice blue")
turtle.down()
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(225)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(125)
turtle.end_fill()

turtle.up()
turtle.color("dark red")
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.down()
turtle.pensize(20)
turtle.forward(100)
turtle.right(90)
turtle.forward(125)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(125)

turtle.color("azure3")
turtle.pensize(5)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(125)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(125)

turtle.right(180)
turtle.forward(25)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(75)

turtle.right(90)
turtle.forward(125)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(125)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(125)
turtle.right(90)
turtle.forward(25)
turtle.right(90)

turtle.right(180)
turtle.up()
turtle.forward(340)
turtle.right(90)
turtle.forward(90)
turtle.right(85)
turtle.down()
turtle.pensize(30)
turtle.color("blue")
turtle.forward(135)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
