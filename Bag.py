import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.setup(800, 600)

# Draw plastic bag
bag = turtle.Turtle()
bag.speed(1)
bag.color("white")
bag.fillcolor("white")
bag.begin_fill()
bag.circle(100)
bag.end_fill()

# Draw bag handle
bag.penup()
bag.goto(-35, 120)
bag.pendown()
bag.color("black")
bag.width(5)
bag.forward(70)

# Draw market scene
market = turtle.Turtle()
market.speed(1)
market.color("green")
market.penup()
market.goto(-200, -100)
market.pendown()
market.begin_fill()
market.forward(400)
market.left(90)
market.forward(200)
market.left(90)
market.forward(400)
market.end_fill()

# Draw market products
product = turtle.Turtle()
product.speed(1)
product.color("red")
product.penup()
product.goto(-150, -50)
product.pendown()
product.begin_fill()
product.circle(20)
product.end_fill()

product.penup()
product.goto(50, -50)
product.pendown()
product.begin_fill()
product.circle(30)
product.end_fill()

product.penup()
product.goto(150, -50)
product.pendown()
product.begin_fill()
product.circle(20)
product.end_fill()

# Hide turtles
bag.hideturtle()
market.hideturtle()
product.hideturtle()

# Keep window open
turtle.done()
```

