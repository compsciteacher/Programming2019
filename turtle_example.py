#HCD
#turtle example
#9/13/19

import turtle,random #always get the turtle
#--------screen-----
screen=turtle.Screen()
screen.bgcolor("green")
screen.screensize(800,800)

#--------make two turtles-----
bob=turtle.Turtle()
jenny=turtle.Turtle()
bob.color('orange')
jenny.color('white')
bob.pensize(5)
jenny.pensize(2)

bob.speed(10000000000000000000000)

#--------movement-----

for i in range(4): #run 1000 times
    bob.forward(100)
    bob.rt(90)
for x in range(4):
    jenny.forward(200)
    jenny.left(90)

screen.exitonclick()