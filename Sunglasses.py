import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")  # Background color
screen.title("Sunglasses Design")  # Title of the window

# Function to draw the frame of the sunglasses
def draw_frame(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.pensize(5)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(50, 180)  # Left lens
    turtle.forward(20)  # Bridge
    turtle.circle(50, 180)  # Right lens
    turtle.forward(20)
    turtle.end_fill()

# Function to draw the lenses
def draw_lenses(x, y):
    turtle.penup()
    turtle.goto(x, y - 50)  # Move down to lens position
    turtle.pendown()
    turtle.color("darkgray")
    turtle.fillcolor("darkgray")
    turtle.begin_fill()
    turtle.circle(50)  # Left lens
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(x + 70, y - 50)  # Move to right lens position
    turtle.pendown()
    turtle.fillcolor("darkgray")
    turtle.begin_fill()
    turtle.circle(50)  # Right lens
    turtle.end_fill()

# Function to draw the temples
def draw_temples():
    turtle.penup()
    turtle.goto(-40, -10)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(-60)  # Left temple
    turtle.penup()
    turtle.goto(90, -10)
    turtle.pendown()
    turtle.forward(60)  # Right temple

# Draw the sunglasses
turtle.speed(5)  # Speed up drawing
draw_frame(0, 0)
draw_lenses(0, 0)
draw_temples()

# Draw border
turtle.penup()
turtle.goto(-100, 60)  # Position for border
turtle.pendown()
turtle.pensize(3)
turtle.color("black")
turtle.goto(100, 60)  # Top border
turtle.goto(100, -100)  # Right border
turtle.goto(-100, -100)  # Bottom border
turtle.goto(-100, 60)  # Left border

# Add title text
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.color("navy")
turtle.write("Stylish Sunglasses", align="center", font=("Arial", 16, "bold"))

# Add additional text
turtle.penup()
turtle.goto(0, -120)
turtle.pendown()
turtle.color("black")
turtle.write("Enjoy the sunshine!", align="center", font=("Arial", 12, "normal"))

# Complete drawing
turtle.hideturtle()
turtle.done()
