import turtle

# Setup the screen with a new background color
screen = turtle.Screen()
screen.bgcolor("lightgrey")

# Create turtle for drawing
pen = turtle.Turtle()
pen.speed(5)

# Function to draw a 3D circle with shadow
def draw_3d_circle(color, shadow_color, radius, x, y, offset):
    # Draw shadow
    pen.penup()
    pen.goto(x + offset, y - offset)
    pen.pendown()
    pen.color(shadow_color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

    # Draw actual circle
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw the face with 3D effect (shadow)
draw_3d_circle("yellow", "darkgoldenrod", 100, 0, -100, 10)  # Head

# Draw eyes with 3D effect
draw_3d_circle("white", "lightgrey", 20, -40, 50, 5)  # Left eye white
draw_3d_circle("white", "lightgrey", 20, 40, 50, 5)   # Right eye white
draw_3d_circle("black", "grey", 10, -40, 60, 3)       # Left eye pupil
draw_3d_circle("black", "grey", 10, 40, 60, 3)        # Right eye pupil

# Draw mouth with 3D effect (shadow under the mouth arc)
pen.penup()
pen.goto(-40, 15)
pen.pendown()
pen.color("grey")
pen.setheading(-60)
pen.circle(40, 120)  # Mouth shadow

pen.penup()
pen.goto(-40, 20)
pen.pendown()
pen.color("red")
pen.setheading(-60)
pen.circle(40, 120)  # Mouth arc

# Draw nose with 3D effect
draw_3d_circle("orange", "darkorange", 10, 0, 40, 3)

# Draw ears with 3D effect
draw_3d_circle("yellow", "darkgoldenrod", 30, -100, 0, 5)  # Left ear
draw_3d_circle("yellow", "darkgoldenrod", 30, 100, 0, 5)   # Right ear

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()
