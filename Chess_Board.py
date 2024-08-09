import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Stylish Chess Board")
wn.bgcolor("#8099c1")

# Create a turtle to draw the board
drawer = turtle.Turtle()
drawer.speed(0)  # Fastest drawing speed
drawer.pensize(2)  # Thicker pen size for drawing
drawer.color("black")  # Default pen color

# Set up the square size and start position
square_size = 50
start_x = -200
start_y = 200

# Function to draw a single square with a border
def draw_square(x, y, color):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.begin_fill()
    drawer.fillcolor(color)
    for _ in range(4):
        drawer.forward(square_size)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

# Function to draw a border around the board
def draw_border():
    drawer.penup()
    drawer.goto(start_x - 10, start_y + 10)
    drawer.pendown()
    drawer.color("darkblue")
    for _ in range(4):
        drawer.forward(square_size * 8 + 20)
        drawer.right(90)
    drawer.penup()
    drawer.color("black")  # Reset pen color

# Function to display a heading
def display_heading():
    drawer.penup()
    drawer.goto(0, start_y + 70)
    drawer.color("darkred")
    drawer.write("Stylish Chess Board", align="center", font=("Arial", 24, "bold"))
    drawer.color("black")  # Reset pen color

# Function to draw some fun elements
def draw_fun():
    drawer.penup()
    drawer.goto(start_x - 30, start_y - (square_size * 8) - 40)
    drawer.color("purple")
    drawer.write("Enjoy the Game!", align="left", font=("Comic Sans MS", 16, "italic"))
    drawer.color("black")  # Reset pen color

# Draw the chess board with stylish borders
for row in range(8):
    for col in range(8):
        x = start_x + col * square_size
        y = start_y - row * square_size
        color = "gray" if (row + col) % 2 == 0 else "white"
        draw_square(x, y, color)

# Draw the border around the chess board
draw_border()

# Display the heading
display_heading()

# Draw fun elements
draw_fun()

# Hide the turtle and display the window
drawer.hideturtle()
wn.mainloop()
