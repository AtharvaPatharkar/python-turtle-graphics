import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle object
t = turtle.Turtle()
t.speed(5)

# Draw the border
t.penup()
t.goto(-300, 250)
t.pendown()
t.pensize(5)
t.color("black")
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(500)
    t.right(90)

# Draw the table fan base
t.penup()
t.goto(-50, -50)
t.pendown()
t.color("grey")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the fan stand
t.penup()
t.goto(0, -50)
t.pendown()
t.pensize(10)
t.color("grey")
t.setheading(90)
t.forward(100)

# Draw the fan blades
t.pensize(5)
t.color("darkblue")

for i in range(4):
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.setheading(90 * i)
    t.forward(100)
    t.right(30)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(30)
    t.forward(100)

# Draw the home-room walls
t.penup()
t.goto(-250, -200)
t.pendown()
t.pensize(5)
t.color("brown")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

# Draw the window
t.penup()
t.goto(-230, -100)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()

# Draw the window panes
t.color("black")
t.pensize(2)
t.forward(25)
t.right(90)
t.forward(50)
t.backward(25)
t.right(90)
t.forward(25)
t.backward(50)

# Draw the door
t.penup()
t.goto(-200, -200)
t.pendown()
t.color("darkred")
t.begin_fill()
t.setheading(90)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.end_fill()

# Draw the door knob
t.penup()
t.goto(-180, -160)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(5)
t.end_fill()

# Draw the title
t.penup()
t.goto(-50, 220)
t.pendown()
t.color("black")
t.write("Home with Table Fan", align="center", font=("Arial", 24, "bold"))

# Draw text labels
t.penup()
t.goto(-250, -220)
t.pendown()
t.write("Home Room", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(0, -180)
t.pendown()
t.write("Table Fan", align="center", font=("Arial", 14, "normal"))

t.hideturtle()
turtle.done()
