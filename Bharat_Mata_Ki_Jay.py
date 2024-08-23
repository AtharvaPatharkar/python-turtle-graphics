import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(18)
turtle.bgcolor("black")

def Bharat():
    t.color("orange")
    

    # Move to starting position
    t.penup()
    t.goto(-500, 300)
    t.pendown()

    # Draw the letter "भ"
    t.circle(-25, 450)
    t.forward(70)
    t.circle(-25, 270)
    t.forward(70)
    t.left(90)
    t.forward(65)
    t.right(180)
    t.forward(110)
    t.penup()
    t.goto(-480, 300)
    t.left(90)
    t.pendown()
    t.forward(340)

    # Move to the next position
    t.penup()
    t.goto(-380, 300)
    t.pendown()

    # Draw the letter "ा"
    t.right(90)
    t.forward(115)

    # Move to the next position
    t.penup()
    t.goto(-320, 300)
    t.pendown()

    # Draw the letter "र"
    t.left(90)
    t.circle(-30, 225)
    t.left(180)
    t.forward(90)

    # Move to the next position
    t.penup()
    t.goto(-160, 300)
    t.pendown()

    # Draw the letter "त"
    t.left(45)
    t.right(90)
    t.forward(110)
    t.backward(70)
    t.right(90)
    t.forward(70)
    t.left(90)
    t.forward(70)

def Mata():
    t.color("white")
    # Move to starting position for "म"
    t.penup()
    t.goto(-160, 100)
    t.pendown()

    # Draw the letter "म"
    t.forward(90)
    t.circle(-30, 270)
    t.forward(100)
    t.left(90)
    t.forward(60)
    t.right(180)
    t.forward(110)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.left(90)
    t.forward(320)

    # Move to the next position for "ा"
    t.penup()
    t.goto(-50, 100)
    t.pendown()

    # Draw the letter "ा"
    t.right(90)
    t.forward(110)

    # Move to the next position for "त"
    t.penup()
    t.goto(50, 100)
    t.pendown()

    # Draw the letter "त"
    t.left(360)
    t.forward(110)
    t.backward(70)
    t.right(90)
    t.forward(70)
    t.left(90)
    t.forward(70)

    # Move to the next position for "ा"
    t.penup()
    t.goto(100, 100)
    t.pendown()

    # Draw the letter "ा"
    t.forward(110)

    # Move to the next position for "क"
    t.penup()
    t.goto(250, 100)
    t.pendown()

    # Draw the letter "क"
    t.forward(110)
    t.backward(55)
    t.circle(-30)
    t.circle(30)
    t.penup()
    t.goto(200, 100)
    t.pendown()
    t.left(90)
    t.forward(200)

    # Move to the next position for "ी"
    t.penup()
    t.goto(280, 100)
    t.pendown()

    # Draw the letter "ी"
    t.right(180)
    t.circle(-40, 180)
    t.forward(10)
    t.circle(-40, 90)
    t.forward(150)

def Jay():
    t.color("green")
    # Draw the letter "जय"
    t.penup()
    t.goto(200, -100)  # Adjusted position as requested
    t.pendown()

    # Draw the letter "ज"
    t.right(270)
    t.forward(300)

    t.penup()
    t.goto(200, -150)  # Adjusted position as requested
    t.pendown()

    t.right(90)
    t.circle(30, 180)
    t.right(90)
    t.forward(55)
    t.right(90)
    t.forward(60)
    t.backward(110)

    # Move to the next position for "य"
    t.penup()
    t.goto(400, -100)  # Adjusted position as requested
    t.pendown()

    # Draw the letter "य"
    t.right(270)
    t.circle(-30, 270)
    t.right(180)
    t.circle(70, 135)

    t.left(45)
    t.forward(80)
    t.backward(110)

# Call the functions to draw the text
Bharat()
Mata()
Jay()

# Hide the turtle
t.hideturtle()

# Complete the drawing
turtle.done()
