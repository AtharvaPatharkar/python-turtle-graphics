import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Flower Design with Border, 3D Effects, and Shapes")

# Create a turtle for drawing flowers
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)

# Function to draw a petal
def draw_petal(t, radius, angle):
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

# Function to draw a flower
def draw_flower(t, radius, angle, petals, color):
    t.color(color)
    for _ in range(petals):
        draw_petal(t, radius, angle)
        t.left(360 / petals)

# Function to draw a border with 3D effect
def draw_border():
    border_turtle = turtle.Turtle()
    border_turtle.speed(0)
    border_turtle.penup()
    border_turtle.goto(-300, 300)
    border_turtle.pendown()

    # Draw 3D border
    border_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for i in range(7):
        border_turtle.color(border_colors[i])
        border_turtle.pensize(5 + i)
        for _ in range(4):
            border_turtle.forward(600 - (i * 10))
            border_turtle.right(90)
        border_turtle.penup()
        border_turtle.goto(-300 + (i * 5), 300 - (i * 5))
        border_turtle.pendown()

# Function to draw random flowers with different colors and sizes
def draw_random_flowers():
    colors = ["red", "blue", "yellow", "purple", "orange", "pink", "green"]
    for _ in range(5):
        flower_turtle.penup()
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        flower_turtle.goto(x, y)
        flower_turtle.pendown()

        radius = random.randint(20, 50)
        petals = random.randint(6, 10)
        angle = random.randint(60, 90)
        color = random.choice(colors)

        draw_flower(flower_turtle, radius, angle, petals, color)

# Function to draw a 3D flower shape
def draw_3d_flower_shape():
    shape_turtle = turtle.Turtle()
    shape_turtle.speed(0)
    shape_turtle.penup()
    shape_turtle.goto(0, -200)
    shape_turtle.pendown()
    shape_turtle.color("gold")
    shape_turtle.begin_fill()
    for _ in range(36):
        shape_turtle.forward(200)
        shape_turtle.left(170)
    shape_turtle.end_fill()

# Draw everything
draw_border()
draw_3d_flower_shape()
draw_random_flowers()

# Hide the turtle
flower_turtle.hideturtle()

# Keep the window open
turtle.done()
