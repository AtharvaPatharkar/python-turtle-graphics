from turtle import *

# set background color, speed, and hide the turtle 
bgcolor("black")
speed(0)
hideturtle()

# Draw the border
penup()
goto(-320, 320)  # Move the turtle to the top-left corner
pendown()
color("white")
pensize(4)

# Draw a square border
for _ in range(4):
    forward(700)
    right(90)

# the colors being used (change them as you wish!)
Colors = ["yellow", "purple", "red", "green", "pink", "blue"]

# repeat x times
x = 100
penup()
goto(0, 0)
pendown()

for i in range(x):
    for col in Colors:
        color(col)
        circle(200 - i, 100)
        lt(90)
        circle(200 - i, 100)
        rt(60)

# Display completion message
penup()
goto(0, 350)
pendown()
color("white")
write("Drawing Completed", align="center", font=("Arial", 24, "bold"))

done()

