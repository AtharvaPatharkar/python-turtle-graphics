import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Mobile Phone with Turtle Graphics")
screen.bgcolor("lightblue")

# Create a turtle object for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw the border of the phone
def draw_border():
    pen.penup()
    pen.goto(-100, 200)
    pen.pendown()
    pen.pensize(3)
    pen.color("black")
    pen.fillcolor("gray")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.right(90)
        pen.forward(400)
        pen.right(90)
    pen.end_fill()

# Draw the screen of the phone
def draw_screen():
    pen.penup()
    pen.goto(-80, 180)
    pen.pendown()
    pen.color("black")
    pen.fillcolor("white")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(160)
        pen.right(90)
        pen.forward(360)
        pen.right(90)
    pen.end_fill()

# Draw the buttons on the phone
def draw_buttons():
    pen.penup()
    pen.goto(-30, -190)
    pen.pendown()
    pen.color("black")
    pen.fillcolor("darkgray")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

    pen.penup()
    pen.goto(0, -190)
    pen.pendown()
    pen.color("black")
    pen.fillcolor("darkgray")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

    pen.penup()
    pen.goto(30, -190)
    pen.pendown()
    pen.color("black")
    pen.fillcolor("darkgray")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

# Draw a title on the screen
def draw_title():
    pen.penup()
    pen.goto(0, 140)
    pen.pendown()
    pen.color("black")
    pen.write("Mobile Phone", align="center", font=("Arial", 16, "bold"))

# Draw a 3D effect by adding shadows
def draw_3d_effect():
    pen.penup()
    pen.goto(-105, 205)
    pen.pendown()
    pen.pensize(1)
    pen.color("black")
    pen.fillcolor("darkgray")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(210)
        pen.right(90)
        pen.forward(410)
        pen.right(90)
    pen.end_fill()

# Create an animation effect by moving a shape
def animate_shape():
    shape = turtle.Turtle()
    shape.shape("circle")
    shape.color("red")
    shape.penup()
    shape.goto(0, 0)

    for _ in range(36):
        shape.forward(10)
        shape.right(10)

# Draw all components
draw_3d_effect()
draw_border()
draw_screen()
draw_buttons()
draw_title()
animate_shape()

# Keep the window open
turtle.done()
