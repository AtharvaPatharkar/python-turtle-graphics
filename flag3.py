import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Scenery with Indian Flag")
screen.bgcolor("skyblue")

# Function to draw a cloud
def draw_cloud(x, y):
    cloud = turtle.Turtle()
    cloud.speed(0)
    cloud.penup()
    cloud.goto(x, y)
    cloud.pendown()
    cloud.color("white")
    cloud.begin_fill()
    for _ in range(6):
        cloud.circle(20, 180)
        cloud.right(120)
    cloud.end_fill()
    cloud.hideturtle()

# Function to draw a tree
def draw_tree(x, y):
    tree = turtle.Turtle()
    tree.speed(0)
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    tree.color("brown")
    tree.begin_fill()
    for _ in range(2):
        tree.forward(20)
        tree.right(90)
        tree.forward(60)
        tree.right(90)
    tree.end_fill()
    tree.goto(x + 10, y)
    tree.color("green")
    tree.begin_fill()
    tree.circle(30)
    tree.end_fill()
    tree.hideturtle()

# Function to draw a house
def draw_house(x, y):
    house = turtle.Turtle()
    house.speed(0)
    house.penup()
    house.goto(x, y)
    house.pendown()
    house.color("blue")
    house.begin_fill()
    for _ in range(4):
        house.forward(100)
        house.right(90)
    house.end_fill()
    house.right(90)
    house.forward(100)
    house.color("red")
    house.begin_fill()
    for _ in range(3):
        house.forward(100)
        house.right(120)
    house.end_fill()
    house.hideturtle()

# Function to draw a flower
def draw_flower(x, y):
    flower = turtle.Turtle()
    flower.speed(0)
    flower.penup()
    flower.goto(x, y)
    flower.pendown()
    flower.color("red")
    flower.begin_fill()
    for _ in range(36):
        flower.forward(50)
        flower.right(45)
        flower.forward(50)
        flower.left(90)
        flower.forward(50)
        flower.right(45)
        flower.forward(50)
        flower.left(90)
        flower.right(10)
    flower.end_fill()
    flower.color("green")
    flower.begin_fill()
    flower.right(90)
    flower.forward(30)
    flower.left(90)
    flower.forward(10)
    flower.left(90)
    flower.forward(30)
    flower.left(90)
    flower.forward(10)
    flower.left(90)
    flower.forward(30)
    flower.end_fill()
    flower.hideturtle()

# Function to draw a road
def draw_road(x, y, width, height):
    road = turtle.Turtle()
    road.speed(0)
    road.penup()
    road.goto(x, y)
    road.pendown()
    road.color("gray")
    road.begin_fill()
    for _ in range(2):
        road.forward(width)
        road.right(90)
        road.forward(height)
        road.right(90)
    road.end_fill()
    road.hideturtle()

# Draw clouds in the background
draw_cloud(-200, 150)
draw_cloud(0, 170)
draw_cloud(200, 150)
draw_cloud(-100, 120)
draw_cloud(100, 120)

# Set up the turtle for the flag
flag = turtle.Turtle()
flag.speed(3)

# Function to draw a rectangle
def draw_rectangle(color, width, height):
    flag.begin_fill()
    flag.color(color)
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()
    flag.forward(width)

# Draw the saffron rectangle
flag.penup()
flag.goto(-150, 100)
flag.pendown()
draw_rectangle("#FF9933", 300, 60)

# Draw the white rectangle
flag.penup()
flag.goto(-150, 40)
flag.pendown()
draw_rectangle("white", 300, 60)

# Draw the green rectangle
flag.penup()
flag.goto(-150, -20)
flag.pendown()
draw_rectangle("#138808", 300, 60)

# Draw the Ashoka Chakra
flag.penup()
flag.goto(0, -20)
flag.pendown()
flag.color("#000080")
flag.circle(30)

# Draw the 24 spokes
flag.penup()
flag.goto(0, 10)
flag.pendown()
for _ in range(24):
    flag.forward(30)
    flag.backward(30)
    flag.right(15)

# Hide the turtle for the flag
flag.hideturtle()

# Draw a tree
draw_tree(200, -150)

# Draw a house
draw_house(-300, -100)



# Draw a road
draw_road(-400, -200, 800, 100)

# Finish the drawing
turtle.done()
