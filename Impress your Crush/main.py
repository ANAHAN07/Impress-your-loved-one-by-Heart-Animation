import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.penup()
t.color("#ffb6c1")

scale = 15

for i in range(360):
    angle = math.radians(i)
    
    x = 16 * (math.sin(angle) ** 3) * scale
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle)) * scale\
         
    t.goto(x, y)
    t.write("I Love You", align="center", font=("Arial", 8, "bold"))

t.penup()
t.goto(0, -20)
t.color("white")
t.write("I Love You ❤️", align="center", font=("Arial", 20, "bold"))     # instead of "I Love You ❤️", you can write your own message here

turtle.done()