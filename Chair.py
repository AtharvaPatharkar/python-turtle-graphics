import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color

# Create turtle object
chair = turtle.Turtle()
chair.speed(5)

# Function to draw the border
def draw_border():
    chair.penup()
    chair.goto(-300, 300)
    chair.pendown()
    chair.pensize(5)
    chair.pencolor("darkgreen")
    for _ in range(4):
        chair.forward(600)
        chair.right(90)

# Function to draw the seat of the chair
def draw_seat():
    chair.penup()
    chair.goto(-100, 0)
    chair.pendown()
    chair.pensize(2)
    chair.pencolor("black")
    chair.fillcolor("brown")
    chair.begin_fill()
    for _ in range(2):
        chair.forward(200)
        chair.right(90)
        chair.forward(50)
        chair.right(90)
    chair.end_fill()

# Function to draw the backrest of the chair
def draw_backrest():
    chair.penup()
    chair.goto(-100, 0)
    chair.pendown()
    chair.fillcolor("saddlebrown")
    chair.begin_fill()
    for _ in range(2):
        chair.forward(200)
        chair.left(90)
        chair.forward(100)
        chair.left(90)
    chair.end_fill()

# Function to draw chair legs
def draw_legs():
    chair.penup()
    chair.goto(-100, -50)
    chair.pendown()
    chair.fillcolor("brown")
    
    # Left front leg
    chair.begin_fill()
    for _ in range(2):
        chair.forward(20)
        chair.right(90)
        chair.forward(100)
        chair.right(90)
    chair.end_fill()

    # Right front leg
    chair.penup()
    chair.goto(80, -50)
    chair.pendown()
    chair.begin_fill()
    for _ in range(2):
        chair.forward(20)
        chair.right(90)
        chair.forward(100)
        chair.right(90)
    chair.end_fill()

    # Left back leg
    chair.penup()
    chair.goto(-100, 100)
    chair.pendown()
    chair.begin_fill()
    for _ in range(2):
        chair.forward(20)
        chair.right(90)
        chair.forward(150)
        chair.right(90)
    chair.end_fill()

    # Right back leg
    chair.penup()
    chair.goto(80, 100)
    chair.pendown()
    chair.begin_fill()
    for _ in range(2):
        chair.forward(20)
        chair.right(90)
        chair.forward(150)
        chair.right(90)
    chair.end_fill()

# Function to add text
def add_text():
    chair.penup()
    chair.goto(-50, -180)  # Position of the text
    chair.pendown()
    chair.pencolor("darkblue")
    chair.write("Simple Chair", font=("Arial", 24, "bold"))

# Call functions to draw the chair and text
draw_border()
draw_seat()
draw_backrest()
draw_legs()
add_text()

# Hide the turtle
chair.hideturtle()

# Keep the window open
turtle.done()
