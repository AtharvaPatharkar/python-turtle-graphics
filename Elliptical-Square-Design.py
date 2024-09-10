import turtle
import math

# Function to draw a square
def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Function to draw ellipse
def draw_ellipse(t, radius_x, radius_y, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(360):
        t.forward(2 * math.pi * radius_x / 360)
        t.left(1)
    t.goto(t.xcor() - radius_y, t.ycor()) # To make the shape more elliptical
    t.end_fill()

# Setting up the screen
screen = turtle.Screen()
screen.bgcolor("lightgreen") 
screen.title("Enhanced Elliptical Square Design")

# Create turtle object
t = turtle.Turtle()
t.speed(0)

# Draw 3D border
def draw_3D_border(t):
    border_color = "darkblue"
    t.penup()
    t.goto(-300, 300)
    t.pendown()
    t.pensize(6)
    t.color(border_color)
    for _ in range(2):
        t.forward(600)
        t.right(90)
        t.forward(600)
        t.right(90)

# Draw elliptical square pattern
def draw_elliptical_square_design():
    colors = ["red", "green", "blue", "orange", "yellow", "purple", 
              "cyan", "magenta", "pink", "lightblue", "darkgreen", "brown", "lightyellow"]
    num_layers = 20  # Increased layers
    size = 50
    for i in range(num_layers):
        t.penup()
        t.goto(-size - (i * 15), size + (i * 15))
        t.pendown()
        t.pensize(2)
        draw_square(t, size + i * 30, colors[i % len(colors)])  # Alternating colors for squares
        t.penup()
        t.goto(0, -(i * 10))  # Adjusting position for ellipse
        t.pendown()
        draw_ellipse(t, size - i * 3, size // 2, colors[(i + 3) % len(colors)])  # Ellipse with varied radius

# Adding text and title
def add_text_and_title():
    t.penup()
    t.goto(-250, 350)
    t.pendown()
    t.color("darkblue")
    t.write("Enhanced Elliptical Square 3D Design", font=("Arial", 26, "bold"))

    t.penup()
    t.goto(-150, -350)
    t.pendown()
    t.write("Design by AP", font=("Arial", 18, "italic"))

# Call the functions
draw_3D_border(t)
draw_elliptical_square_design()
add_text_and_title()

# Hide the turtle
t.hideturtle()

# Keep the window open until clicked
turtle.done()
