#HCD
#turtle input v.1
#9/17/19

import turtle,random #always get the turtle
#--------screen-----
screen=turtle.Screen()
screen.bgcolor("green")
screen.screensize(800,800)

#--------make a turtle-----
bob=turtle.Turtle()
bob.color('orange')
bob.pensize(5)
bob.speed(10000000000000000000000)
#--------actual movement-----
dist=30 #starting distance to move
for i in range(1000): #run 1000 times
    #print(bob.ycor())
    bob.forward(dist) #bob moves whatever random distance is
    bob.rt(random.randint(1,360)) #turns random degrees
    dist+=random.randint(1,15)
    if dist>=125: #max distance of 125, then resets to 50
        dist=50
    if bob.xcor()>400 or bob.xcor()<-400: #if bob goes outside screen resets to 0,0
        bob.setpos(0,0)
    if bob.ycor()>400 or bob.ycor()<-400:
        bob.setpos(0,0)

screen.exitonclick()