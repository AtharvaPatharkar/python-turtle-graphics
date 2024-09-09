from turtle import Screen, Turtle

def curved_box(t, sides):
    for _ in range(sides):
        t.circle(90, extent=90)
        t.forward(120)
    t.circle(90, extent=90)

def snake(t, color):
    t.penup()
    t.backward(16)
    t.left(90)
    t.forward(16)
    t.right(90)
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()
    t.forward(64)
    curved_box(t, 2)
    t.forward(44)
    t.left(90)
    t.forward(152)
    t.right(90)
    t.forward(16)
    t.right(90)
    t.forward(204)
    curved_box(t, 1)
    t.forward(44)
    t.left(90)
    t.forward(60)
    t.circle(-90, extent=90)
    t.forward(64)
    t.end_fill()

    t.penup()
    t.backward(86)
    t.left(90)
    t.forward(224)
    t.dot(48, 'white')
    t.backward(224)
    t.right(90)
    t.forward(86)
    t.pendown()

def draw_border(t, width, height):
    t.penup()
    t.goto(-width//2, height//2)  # Top-left corner
    t.pendown()
    t.pencolor('white')  # Set border color
    t.pensize(3)  # Set pen size for border
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.penup()
    t.home()

screen = Screen()
screen.bgcolor("Black")
turtle = Turtle()

# Draw the border
border_width = screen.window_width() - 0
border_height = screen.window_height() - 0
draw_border(turtle, border_width, border_height)

# Set pen color for the snake
turtle.pencolor('#3774A8')

# Draw the first snake
snake(turtle, '#3774A8')

# Draw the second snake
turtle.left(180)
turtle.pencolor('#F6D646')
snake(turtle, '#F6D646')

screen.exitonclick()
