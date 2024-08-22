import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Turtle Graphics House - January 2024")
screen.bgcolor("skyblue")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(2)

# Function to draw a border
def draw_border():
    pen.penup()
    pen.goto(-250, 250)
    pen.pendown()
    pen.color("black")
    for _ in range(4):
        pen.forward(500)
        pen.right(90)

# Function to draw a heading
def draw_heading():
    pen.penup()
    pen.goto(0, 260)
    pen.color("black")
    pen.write("My Turtle Graphics House", align="center", font=("Arial", 24, "bold"))



# Function to draw the house
def draw_house():
    # Draw the base of the house
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.color("blue")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(150)
        pen.left(90)
    pen.end_fill()
    
    # Draw the roof
    pen.penup()
    pen.goto(-130, 100)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.goto(0, 200)
    pen.goto(130, 100)
    pen.goto(-130, 100)
    pen.end_fill()

# Function to draw text
def draw_text():
    pen.penup()
    pen.goto(0, -200)
    pen.color("black")
    pen.write("Home Sweet Home", align="center", font=("Arial", 16, "bold"))

# Function to draw the door
def draw_door():
    pen.penup()
    pen.goto(-30, -50)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    pen.setheading(90)
    pen.forward(60)
    pen.right(90)
    pen.forward(40)
    pen.right(90)
    pen.forward(60)
    pen.end_fill()

# Function to draw windows
def draw_windows():
    pen.penup()
    pen.goto(-40, 40)
    pen.pendown()
    pen.color("lightblue")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(40)
        pen.right(90)
    pen.end_fill()
    
    pen.penup()
    pen.goto(60, 40)
    pen.pendown()
    pen.begin_fill()
    for _ in range(4):
        pen.forward(40)
        pen.right(90)
    pen.end_fill()

# Draw all elements
draw_border()
draw_heading()

draw_house()
draw_door()
draw_windows()
draw_text()

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
