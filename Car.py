import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Car")
wn.bgcolor("lightblue")

# Create the turtle for drawing
car = turtle.Turtle()
car.speed(0)  # Fastest speed for drawing

# Draw the road
def draw_road():
    road = turtle.Turtle()
    road.color("gray")
    road.begin_fill()
    road.penup()
    road.goto(-1000, -100)
    road.pendown()
    road.forward(2000)
    road.right(90)
    road.forward(50)
    road.right(90)
    road.forward(2000)
    road.right(90)
    road.forward(50)
    road.end_fill()
    road.hideturtle()

# Draw the car body
def draw_car_body():
    car.color("black", "red")
    car.begin_fill()
    car.penup()
    car.goto(-100, -50)
    car.pendown()
    car.forward(200)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(200)
    car.left(90)
    car.forward(50)
    car.end_fill()
    car.backward(50)
    car.left(90)

# Draw the car top
def draw_car_top():
    car.color("black", "orange")
    car.begin_fill()
    car.penup()
    car.left(45)
    car.forward(70)
    car.right(45)
    car.forward(100)
    car.right(45)
    car.forward(70)
    car.end_fill()

# Draw the car windows
def draw_car_windows():
    car.color("black", "lightblue")
    car.begin_fill()
    car.penup()
    car.goto(-55, 0)
    car.pendown()
    car.right(135)
    car.forward(55)
    car.right(90)
    car.forward(100)
    car.right(90)
    car.forward(55)
    car.end_fill()

# Draw the car wheels
def draw_wheel(x, y):
    car.penup()
    car.goto(x, y)
    car.pendown()
    car.color("black", "black")
    car.begin_fill()
    car.circle(20)
    car.end_fill()

# Add text
def add_text():
    text = turtle.Turtle()
    text.speed(0)
    text.color("black")
    text.penup()
    text.goto(0, 150)
    text.write("My Car", align="center", font=("Arial", 24, "bold"))
    text.hideturtle()

# Draw the garden
def draw_garden():
    garden = turtle.Turtle()
    garden.color("green")
    garden.penup()
    garden.goto(-1000, -150)
    garden.pendown()
    garden.begin_fill()
    garden.forward(2100)
    garden.right(90)
    garden.forward(150)
    garden.right(90)
    garden.forward(2100)
    garden.right(90)
    garden.forward(150)
    garden.end_fill()
    garden.hideturtle()

# Draw the sun
def draw_sun():
    sun = turtle.Turtle()
    sun.penup()
    sun.goto(200, 200)
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    sun.circle(50)
    sun.end_fill()
    sun.hideturtle()

# Draw all parts of the car, road, garden, and sun
draw_garden()
draw_road()
draw_car_body()
draw_car_top()
draw_wheel(-70, -70)
draw_wheel(50, -70)
add_text()
draw_sun()

# Hide the car turtle
car.hideturtle()

# Keep the window open
turtle.done()
