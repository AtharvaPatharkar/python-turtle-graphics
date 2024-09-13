import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("#102b0c")

# Create a turtle object for drawing
temple = turtle.Turtle()
temple.speed(3)

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    temple.fillcolor(color)
    temple.begin_fill()
    for _ in range(2):
        temple.forward(width)
        temple.left(90)
        temple.forward(height)
        temple.left(90)
    temple.end_fill()

# Function to draw the base of the temple
def draw_base():
    temple.penup()
    temple.goto(-150, -100)  # Starting position
    temple.pendown()
    draw_rectangle(300, 50, "grey")

# Function to draw pillars
def draw_pillars():
    # First pillar
    temple.penup()
    temple.goto(-120, -50)
    temple.pendown()
    draw_rectangle(30, 100, "white")
    
    # Second pillar
    temple.penup()
    temple.goto(-30, -50)
    temple.pendown()
    draw_rectangle(30, 100, "white")
    
    # Third pillar
    temple.penup()
    temple.goto(60, -50)
    temple.pendown()
    draw_rectangle(30, 100, "white")

# Function to draw the roof
def draw_roof():
    temple.penup()
    temple.goto(-160, 50)
    temple.pendown()
    temple.fillcolor("gold")
    temple.begin_fill()
    for _ in range(3):  # Triangle roof
        temple.forward(320)
        temple.left(120)
    temple.end_fill()

# Function to draw the entrance
def draw_entrance():
    temple.penup()
    temple.goto(-70, -100)
    temple.pendown()
    draw_rectangle(120, 80, "brown")

# Function to draw temple dome
def draw_dome():
    temple.penup()
    temple.goto(-10, 50)
    temple.pendown()
    temple.fillcolor("yellow")
    temple.begin_fill()
    temple.circle(50)  # Dome shape
    temple.end_fill()

# Function to add title and text
def add_text():
    # Title
    temple.penup()
    temple.goto(-300, 300)
    temple.pendown()
    temple.color("darkblue")
    temple.write("Temple", align="center", font=("Arial", 24, "bold"))
    
    # Description text
    temple.penup()
    temple.goto(0, -180)
    temple.pendown()
    temple.color("white")
    temple.write("Created by AP", align="center", font=("Arial", 16, "normal"))

# Draw temple step by step
draw_base()
draw_pillars()
draw_roof()
draw_entrance()
draw_dome()
add_text()

# Hide the turtle and finish
temple.hideturtle()
screen.mainloop()
