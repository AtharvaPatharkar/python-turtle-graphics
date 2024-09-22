import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Beautiful Rainy Day")
screen.bgcolor("sky blue")

# Create turtle object
pen = turtle.Turtle()
pen.speed(10)

# Function to draw a colored semicircle (umbrella top)
def draw_umbrella_top(radius, color):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.setheading(180)
    pen.circle(radius, 180)
    pen.end_fill()

# Function to draw the umbrella handle
def draw_handle():
    pen.penup()
    pen.goto(-20, 0)
    pen.setheading(-90)
    pen.pendown()
    pen.pensize(6)
    pen.pencolor("brown")
    pen.forward(100)
    pen.circle(20, 180)
    pen.hideturtle()

# Draw grass
def draw_grass():
    pen.penup()
    pen.goto(-300, -150)
    pen.setheading(0)
    pen.pendown()
    pen.pensize(2)
    pen.pencolor("green")
    pen.fillcolor("green")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(600)
        pen.right(90)
        pen.forward(150)
        pen.right(90)
    pen.end_fill()

# Draw the rainbow
def draw_rainbow():
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    radius = 200
    pen.penup()
    pen.goto(-250, 100)
    pen.setheading(60)
    for color in colors:
        pen.pendown()
        pen.pencolor(color)
        pen.circle(radius, 180)
        radius -= 10
        pen.penup()
        pen.goto(-250, 100 - (200 - radius))

# Function to draw raindrops
def draw_rain():
    pen.pensize(2)
    pen.pencolor("blue")
    for _ in range(30):
        x = random.randint(-300, 300)
        y = random.randint(50, 300)
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(-90)
        pen.forward(20)

# Function to draw border
def draw_border():
    pen.penup()
    pen.goto(-320, 320)
    pen.setheading(0)
    pen.pendown()
    pen.pensize(5)
    pen.pencolor("black")
    for _ in range(4):
        pen.forward(640)
        pen.right(90)

# Write text
def write_text():
    pen.penup()
    pen.goto(0, -280)
    pen.pendown()
    pen.pencolor("purple")
    pen.write("Enjoy the Rain!", align="center", font=("Arial", 24, "bold"))
    pen.hideturtle()

# Main drawing
def draw_scene():
    draw_grass()
    draw_rainbow()
    draw_umbrella_top(100, "red")
    draw_handle()
    draw_rain()
    draw_border()
    write_text()

# Execute drawing
draw_scene()

# Keep the window open
turtle.done()
