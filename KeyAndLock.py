import turtle

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("lightyellow")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a 3D border
def draw_3d_border(t, width, height, depth, color1, color2):
    t.color(color1)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    t.penup()
    t.forward(depth)
    t.right(90)
    t.forward(depth)
    t.left(90)
    t.pendown()

    t.color(color2)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Function to draw the key
def draw_key(t):
    t.penup()
    t.goto(-200, 50)
    t.pendown()

    # Draw the key handle (circular part)
    t.color("gold")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    # Draw the key shaft
    t.right(90)
    t.forward(100)

    # Draw the key teeth
    for _ in range(2):
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(20)
        t.left(90)

# Function to draw the lock
def draw_lock(t):
    t.penup()
    t.goto(50, -50)
    t.pendown()

    # Draw the lock body
    t.color("darkgray")
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.end_fill()

    # Draw the lock shackle (U-shaped part)
    t.penup()
    t.goto(75, 100)
    t.pendown()
    t.color("gray")
    t.width(10)
    t.circle(50, 180)

# Draw the border with 3D effects
pen.penup()
pen.goto(-300, 250)
pen.pendown()
draw_3d_border(pen, 600, 500, 10, "black", "darkgray")

# Draw the key
pen.width(3)
draw_key(pen)

# Draw the lock
pen.width(3)
draw_lock(pen)

pen.hideturtle()
screen.mainloop()
  
