import turtle
from datetime import datetime

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightyellow")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(10)

# Function to draw a 3D border
def draw_3d_border():
    # First, draw the outer shadow for 3D effect
    drawer.penup()
    drawer.goto(-355, 255)
    drawer.pendown()
    drawer.pensize(7)
    drawer.pencolor("gray")
    for _ in range(2):
        drawer.forward(710)
        drawer.right(90)
        drawer.forward(510)
        drawer.right(90)

    # Then draw the actual border
    drawer.penup()
    drawer.goto(-350, 250)
    drawer.pendown()
    drawer.pensize(5)
    drawer.pencolor("blue")
    for _ in range(2):
        drawer.forward(700)
        drawer.right(90)
        drawer.forward(500)
        drawer.right(90)

# Function to fill the inside of the border with a color
def fill_inside_border(color):
    drawer.penup()
    drawer.goto(-345, 245)
    drawer.pendown()
    drawer.pencolor("green")
    drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(690)
        drawer.right(90)
        drawer.forward(490)
        drawer.right(90)
    drawer.end_fill()

# Function to draw a flower
def draw_flower(x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.pencolor("red")
    drawer.fillcolor("pink")

    # Draw petals
    for _ in range(6):
        drawer.begin_fill()
        drawer.circle(10, steps=6)  # Hexagon petals
        drawer.end_fill()
        drawer.penup()
        drawer.forward(20)
        drawer.right(60)
        drawer.pendown()
    
    # Draw center
    drawer.penup()
    drawer.goto(x + 10, y - 25)
    drawer.pendown()
    drawer.pencolor("yellow")
    drawer.fillcolor("yellow")
    drawer.begin_fill()
    drawer.circle(10)
    drawer.end_fill()

# Function to write "Welcome to this year's" with a more attractive font and color
def write_welcome_message():
    drawer.penup()
    drawer.goto(240, -10)
    drawer.pendown()
    drawer.pensize(4)  # Increased pen size
    drawer.pencolor("darkgreen")
    drawer.write("Welcome\nto this\nyear's", align="center", font=("Courier", 30, "bold italic"))

# Function to write heading with 3D effect
def write_heading():
    drawer.penup()
    drawer.goto(-50, 200)
    drawer.pendown()
    drawer.pencolor("black")
    drawer.write("January 2025", align="center", font=("Arial", 30, "bold"))
    
    drawer.penup()
    drawer.goto(-53, 197)
    drawer.pendown()
    drawer.pencolor("gray")
    drawer.write("January 2025", align="center", font=("Arial", 30, "bold"))

# Function to write days of the week with different colors
def write_weekdays():
    weekdays = [("Sun", "red"), ("Mon", "orange"), ("Tues", "yellow"), 
                ("Wednes", "green"), ("Thurs", "blue"), ("Fri", "indigo"), 
                ("Satur", "violet")]
    start_x = -250
    start_y = 180
    for i, (day, color) in enumerate(weekdays):
        drawer.penup()
        drawer.goto(start_x + i * 90, start_y)
        drawer.pendown()
        drawer.pencolor(color)
        drawer.write(day, align="center", font=("Arial", 12, "bold"))

# Function to draw a single day with 3D effect
def draw_day(x, y, day, color):
    # Shadow for 3D effect
    drawer.penup()
    drawer.goto(x + 15, y - 15)
    drawer.pendown()
    drawer.fillcolor("gray")
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(50)
        drawer.right(90)
    drawer.end_fill()

    # Actual day block
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(50)
        drawer.right(90)
    drawer.end_fill()
    
    # Writing the day number
    drawer.penup()
    drawer.goto(x + 25, y - 40)
    drawer.pencolor("black")
    drawer.write(str(day), align="center", font=("Arial", 12, "bold"))

# Function to draw the entire calendar
def draw_calendar():
    colors = ["lightblue", "lightgreen", "lightpink", "lightcoral", "lightgoldenrodyellow"]
    start_x = -300
    start_y = 120
    day = 1

    for week in range(5):
        for day_index in range(7):
            if day > 31:
                break
            color = colors[day_index % len(colors)]
            draw_day(start_x + day_index * 60, start_y - week * 60, day, color)
            day += 1

# Drawing the 3D border
draw_3d_border()

# Filling the inside of the border with a color
fill_inside_border("lightcyan")

# Drawing flowers in the corners of the border
draw_flower(-360, 270)   # Top-left corner
draw_flower(340, 270)    # Top-right corner
draw_flower(-360, -230)  # Bottom-left corner
draw_flower(340, -230)   # Bottom-right corner

# Writing the heading
write_heading()

# Writing the days of the week
write_weekdays()

# Drawing the calendar
draw_calendar()

# Writing the welcome message
write_welcome_message()

# Hide the turtle and display the result
drawer.hideturtle()
turtle.done()
