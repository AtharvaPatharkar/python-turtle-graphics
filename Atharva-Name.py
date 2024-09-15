import turtle

# Setup the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Atharva")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(5)

# Function to draw a rectangle (border)
def draw_border():
    pen.penup()
    pen.goto(-250, 200)
    pen.pendown()
    pen.pensize(10)
    pen.color("blue")
    for _ in range(2):
        pen.forward(500)
        pen.right(90)
        pen.forward(400)
        pen.right(90)
    pen.penup()

# Function to create 3D text effect
def draw_3d_text(text, color):
    x, y = -200, 0
    offset = 2  # 3D shadow offset

    # Draw the shadow for the 3D effect
    pen.penup()
    pen.goto(x + offset, y - offset)
    pen.color("gray")
    pen.write(text, font=("Arial", 80, "bold"))

    # Draw the actual text
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, font=("Arial", 80, "bold"))

# Main Drawing
draw_border()
draw_3d_text("Atharva", "red")

# Hide the pen
pen.hideturtle()

# Keep the window open
turtle.done()
