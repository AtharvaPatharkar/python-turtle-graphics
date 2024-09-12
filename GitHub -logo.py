import turtle as t

# Set up the screen
t.bgcolor("white")
t.title("GitHub Logo")

# Create a turtle object
pen = t.Turtle()
pen.speed(5)

# Function to draw a circle (for the head of the octocat)
def draw_circle(radius, color):
    pen.penup()
    pen.goto(0, -radius)  # Adjust position to center the circle
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Function to draw the eyes
def draw_eye(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(10)  # Eye size
    pen.end_fill()

# Function to draw the mouth (arc shape)
def draw_mouth():
    pen.penup()
    pen.goto(-50, -30)
    pen.pendown()
    pen.setheading(-60)  # Set the orientation for the arc
    pen.circle(50, 120)  # Draw an arc with radius 50 and 120 degrees

# Function to draw the ears
def draw_ear(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.setheading(0)
    pen.circle(30, 180)  # Half-circle shape for the ear
    pen.end_fill()

# Draw the head of the octocat
draw_circle(100, "black")

# Draw the eyes
pen.color("white")
draw_eye(-40, 50)  # Left eye
draw_eye(40, 50)   # Right eye

# Draw the mouth
pen.color("white")
pen.width(3)
draw_mouth()

# Draw the ears
pen.color("black")
draw_ear(-100, 20)  # Left ear
draw_ear(100, 20)   # Right ear

# Hide the turtle
pen.hideturtle()

# Complete the drawing
t.done()
