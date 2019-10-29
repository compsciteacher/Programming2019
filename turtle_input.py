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

#--------get inputs---------
dist=int(input("How far would you like the turtle to move? "))
turn=int(input("How much would you like the turtle to turn each time? "))
times=int(input("Number of times? "))
#--------actual movement-----

for i in range(times): #run 1000 times
    #print(bob.ycor())
    bob.forward(dist) #bob moves whatever random distance is
    bob.rt(turn) #turns random degrees

screen.exitonclick()