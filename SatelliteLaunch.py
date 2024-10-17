import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("3D Satellite Launch Simulation")
screen.bgcolor("midnight blue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Title
title = turtle.Turtle()
title.hideturtle()
title.penup()
title.color("white")
title.goto(0, 250)
title.write("3D Satellite Launch Simulation", align="center", font=("Arial", 24, "bold"))

# Draw border
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-350, -250)
border.pendown()
border.pensize(3)
for _ in range(2):
    border.forward(700)
    border.left(90)
    border.forward(500)
    border.left(90)

# Star background (randomly scattered stars)
def draw_stars(num_stars):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.color("white")
    star.penup()
    for _ in range(num_stars):
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        star.goto(x, y)
        star.dot(random.randint(2, 4))

# Drawing random stars in the background
draw_stars(50)

# Rocket base
rocket = turtle.Turtle()
rocket.shape("square")
rocket.color("light gray")
rocket.shapesize(stretch_wid=4, stretch_len=2)
rocket.penup()
rocket.goto(0, -200)

# Rocket 3D effect (side shading)
side_shade = turtle.Turtle()
side_shade.shape("square")
side_shade.color("dim gray")
side_shade.shapesize(stretch_wid=4, stretch_len=0.5)
side_shade.penup()
side_shade.goto(20, -200)

# Rocket fire animation
fire = turtle.Turtle()
fire.shape("triangle")
fire.color("orange")
fire.shapesize(stretch_wid=2, stretch_len=1.5)
fire.penup()
fire.goto(0, -260)

# Satellite object
satellite = turtle.Turtle()
satellite.shape("square")
satellite.color("light blue")
satellite.shapesize(stretch_wid=1.5, stretch_len=1.5)
satellite.penup()
satellite.goto(-400, 150)
satellite.hideturtle()

# Message display turtle
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.color("white")
message.goto(0, -270)

# Planet in the background (to simulate depth)
planet = turtle.Turtle()
planet.shape("circle")
planet.color("dark red")
planet.shapesize(stretch_wid=10, stretch_len=10)
planet.penup()
planet.goto(250, 180)

# Function to move the rocket upwards
def launch_rocket():
    message.write("Launching Rocket...", align="center", font=("Arial", 16, "bold"))
    time.sleep(1)
    message.clear()

    for _ in range(40):
        rocket.sety(rocket.ycor() + 5)
        side_shade.sety(side_shade.ycor() + 5)
        fire.sety(fire.ycor() + 5)
        screen.update()
        time.sleep(0.05)

    fire.hideturtle()

    # After launch, move the satellite across the screen
    satellite.showturtle()
    message.write("Deploying Satellite...", align="center", font=("Arial", 16, "bold"))
    for _ in range(100):
        satellite.setx(satellite.xcor() + 5)
        satellite.sety(satellite.ycor() + 1)
        screen.update()
        time.sleep(0.05)

    message.clear()
    message.write("Launch Successful!", align="center", font=("Arial", 16, "bold"))

# Animation for the flame effect
def flame_animation():
    fire.showturtle()
    for _ in range(10):
        fire.color("yellow")
        time.sleep(0.1)
        fire.color("red")
        time.sleep(0.1)
        screen.update()

# Satellite spinning effect for 3D
def satellite_spin():
    for _ in range(36):
        satellite.right(10)
        screen.update()
        time.sleep(0.05)

# Create moving stars to simulate depth (parallax effect)
def moving_stars():
    stars = []
    for _ in range(30):
        star = turtle.Turtle()
        star.shape("circle")
        star.color("white")
        star.penup()
        star.speed(0)
        star.goto(random.randint(-390, 390), random.randint(-290, 290))
        stars.append(star)

    for _ in range(100):  # Move stars across the screen
        for star in stars:
            star.setx(star.xcor() - 2)
            if star.xcor() < -400:
                star.setx(400)
            screen.update()
            time.sleep(0.02)

# Function to run the animation
def satellite_launch():
    flame_animation()
    launch_rocket()
    moving_stars()
    satellite_spin()

# Start the satellite launch animation
satellite_launch()

# Keep the window open
screen.mainloop()
