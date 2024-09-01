import turtle
import random
from datetime import datetime

# Set up the screen
turtle.bgcolor("black")
screen = turtle.Screen()
screen.title("Enhanced Turtle Graphics")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)  # Pen width

# Function to draw a 3D effect border
def draw_3d_border(t, size):
    for i in range(4):
        for j in range(4):
            t.penup()
            t.goto(-size + i*10, -size + j*10)
            t.pendown()
            for _ in range(4):
                t.forward(size - 2 * i * 10)
                t.left(90)

# 3D effect border size
border_size = 35

print("\nProcess START: " + str(datetime.now()))

# Draw the 3D border
draw_3d_border(t, border_size)

# Start drawing the main pattern with 3D effect and color
i = 72
for x in range(4):
    for j in range(i):
        myPenColorR = random.random()
        myPenColorG = random.random()
        myPenColorB = random.random()

        t.pencolor(myPenColorR, myPenColorG, myPenColorB)
        t.forward(150)
        t.right(85)

        # Add 3D effect by drawing shadow lines
        t.penup()
        t.forward(10)  # No angle change
        t.pendown()
        t.pencolor(myPenColorR/2, myPenColorG/2, myPenColorB/2)
        t.forward(125)

    t.left(90)

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))
print("Please close the graphics window to end the program.")

turtle.mainloop()
