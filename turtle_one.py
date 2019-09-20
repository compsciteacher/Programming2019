#HCD
#first turtle
#9/12/19

import turtle, random
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("blue")
wn.screensize(800,800)
x=75

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("white")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.pensize(10)
alex.color("red")

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)
tess.speed(100)# move her away from the origin


y=90
for n in range(1000):
    for i in range(10):
        print(i)
    tess.forward(y)
    tess.right(x)
    x+=random.randint(1,40)
    y+=random.randint(1,10)
    tess.speed(random.randint(1,500))
    if x>120:
        x-=60
    if x<20:
        x+=47
    if y>120:
        y-=50
    if y<20:
        y+=72
    print(x)
alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
