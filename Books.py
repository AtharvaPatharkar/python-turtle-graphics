import turtle

# Function to draw a rectangle (used for book cover)
def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the side of the book (to create a 3D effect)
def draw_side(width, height):
    turtle.fillcolor('grey')
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(45)
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(height)
    turtle.left(135)
    turtle.forward(20)
    turtle.left(45)
    turtle.end_fill()

# Function to draw a book with 3D effect and a design on the cover
def draw_book(x, y, width, height, color, design):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Draw the front cover
    draw_rectangle(color, width, height)

    # Draw the side of the book
    turtle.left(90)
    draw_side(width, height)

    # Add a design on the book cover
    turtle.penup()
    turtle.goto(x + 5, y + height - 30)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.write(design, font=("Arial", 10, "bold"))

# Function to draw a cup of tea
def draw_cup(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(x - 20, y + 30)
    turtle.pendown()
    turtle.circle(20, 180)
    
# Function to draw pen and paper
def draw_pen_paper(x, y):
    # Draw paper
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    
    # Draw pen
    turtle.penup()
    turtle.goto(x + 30, y + 50)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.width(5)
    turtle.forward(80)

# Setup turtle
turtle.speed(3)
turtle.bgcolor("lightblue")
turtle.title("3D Bookshelf with Extras")

# Draw Books with designs on covers
draw_book(-100, 0, 30, 70, 'blue', 'Python')
draw_book(-50, 0, 30, 70, 'red', 'Java')
draw_book(0, 0, 30, 70, 'green', 'HTML')
draw_book(50, 0, 30, 70, 'purple', 'CSS')

# Draw the shelf
turtle.penup()
turtle.goto(-130, -10)
turtle.pendown()
turtle.width(5)
turtle.forward(230)

# Draw Cup of Tea
draw_cup(100, -100)

# Draw Pen and Paper
draw_pen_paper(-150, -150)

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
