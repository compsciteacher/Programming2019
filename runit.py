import turtle

wn = turtle.Screen()

bob = turtle.Turtle()
bob.color("red")

deg = int(input('how many degrees:'))  # enter what degrees to turn
far = int(input('how far to go:'))  # enter how far you want to go
times = int(input('how many times:'))  # enter how many time you want to do this
for x in range(times):
    bob.fd(far)
    bob.right(deg)

wn.exitonclick()