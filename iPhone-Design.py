import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("iPhone Design")

# Create turtle object
pen = turtle.Turtle()
pen.speed(3)
pen.hideturtle()

# Function to draw the iPhone body
def draw_iphone_body():
    pen.penup()
    pen.goto(-120, -240)
    pen.pendown()
    pen.fillcolor("black")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(240)
        pen.circle(30, 90)
        pen.forward(480)
        pen.circle(30, 90)
    pen.end_fill()

# Function to draw the screen
def draw_screen():
    pen.penup()
    pen.goto(-100, -210)
    pen.pendown()
    pen.fillcolor("lightgrey")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(400)
        pen.left(90)
    pen.end_fill()

# Function to draw the home button
def draw_home_button():
    pen.penup()
    pen.goto(-40, -230)
    pen.pendown()
    pen.fillcolor("darkgrey")
    pen.begin_fill()
    pen.circle(40)
    pen.end_fill()

# Function to draw the speaker
def draw_speaker():
    pen.penup()
    pen.goto(-60, 210)
    pen.pendown()
    pen.fillcolor("grey")
    pen.begin_fill()
    pen.forward(120)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(120)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.end_fill()

# Function to draw the front camera
def draw_front_camera():
    pen.penup()
    pen.goto(-10, 180)
    pen.pendown()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

# Function to draw volume buttons
def draw_volume_buttons():
    pen.penup()
    pen.goto(-130, 100)
    pen.pendown()
    pen.fillcolor("darkgrey")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(20)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(-130, 50)
    pen.pendown()
    pen.fillcolor("darkgrey")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(20)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(-130, 0)
    pen.pendown()
    pen.fillcolor("darkgrey")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(20)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()

# Drawing the iPhone design
draw_iphone_body()
draw_screen()
draw_home_button()
draw_speaker()
draw_front_camera()
draw_volume_buttons()

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
