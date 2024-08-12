import turtle
turtle.speed(0)

# Function to draw a designed number
def draw_number(turtle_obj, x, y, number):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("#35b0c2")
    turtle_obj.write(number, align="center", font=("Arial", 12, "bold"))
    
    # Draw a border around the number
    turtle_obj.penup()
    turtle_obj.goto(x -18,  y+25)
    turtle_obj.pendown()
    turtle_obj.color("#01b101")
    turtle_obj.pensize(2)
    for _ in range(4):
        turtle_obj.forward(40)
        turtle_obj.right(90)

# Screen setup
screen = turtle.Screen()
screen.bgcolor("#32b1d1")  # Background color
screen.title("Multiplication Table")

# Turtle setup for table
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw border for table
pen.penup()
pen.goto(-250, 250)
pen.pendown()
pen.color("#b10807")
pen.pensize(5)
pen.begin_fill()
for _ in range(4):
    pen.forward(500)
    pen.right(90)
pen.end_fill()

# Table generation with 3D effects and colors
start_x, start_y = -275, 275
for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        x = start_x + j * 50
        y = start_y - i * 50
        
        # 3D effect shadow
        pen.penup()
        pen.goto(x+2, y-2)
        pen.pendown()
        pen.color("gray")
        draw_number(pen, x + 2, y - 2, result)
        
        # Main text with 3D effect
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("#010101")
        draw_number(pen, x+3, y-3, result)

# Add title text
pen.penup()
pen.goto(0, start_y + 50)
pen.color("darkred")
pen.write("Enjoy the Multiplication Table", align="center", font=("Arial", 18, "bold"))

# Add credit text
pen.penup()
pen.goto(0, start_y - 25)
pen.color("black")
pen.write("Code by AP", align="center", font=("Arial", 14, "italic"))

turtle.done()
