from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

colors = ["gray", "light slate gray", "dark cyan", "medium sea green", "spring green", "dark green", "olive", "dark olive green", "gold", "peru", "orange", "dark orange", "dark red", "rosy brown", "plum", "dark orchid", "medium purple", "dark slate blue"]

direction = [0, 90, 180, 270]

"""def draw_shape(num_sides):
    angle = 360 / num_sides
    for step in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)
        
def draw():
    for side in range(3, 11):
        turtle.color(random.choice(colors))
        draw_shape(side)
        
draw()"""

def random_walk():
    turtle.pensize(10)
    for step in range(200):
        turtle.color(random.choice(colors))
        turtle.forward(30)
        turtle.right(random.choice(direction))

random_walk()
# Objeto pantalla
screen = Screen()
screen.exitonclick()
