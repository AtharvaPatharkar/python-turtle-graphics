import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object for drawing the mango
mango = turtle.Turtle()
mango.shape("turtle")
mango.speed(5)

# Draw the mango shape (oval)
mango.color("orange")
mango.begin_fill()
mango.left(45)
mango.forward(100)
mango.circle(50, 180)
mango.forward(100)
mango.circle(50, 180)
mango.end_fill()

# Draw the mango stem
mango.penup()
mango.goto(35, 135)
mango.pendown()
mango.color("brown")
mango.pensize(5)
mango.left(90)
mango.forward(30)

# Draw the leaf
mango.penup()
mango.goto(35, 165)
mango.pendown()
mango.color("green")
mango.pensize(2)
mango.right(120)
mango.begin_fill()
mango.circle(30, 180)
mango.right(180)
mango.circle(30, 180)
mango.end_fill()

# Hide the turtle
mango.hideturtle()

# Complete the drawing
turtle.done()
