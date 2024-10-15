import turtle
import random
import time

# Setup screen with larger size
wn = turtle.Screen()
wn.title("Life Under the Sea - Code with AP")
wn.bgcolor("darkblue")  # Change the background to a deep-sea blue
wn.setup(width=1000, height=800)  # Larger window
wn.tracer(0)  # Turn off animation to manually control frame updates

# Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.goto(-450, 350)
border_pen.pendown()
border_pen.pensize(3)
border_pen.color("lightblue")
for _ in range(2):
    border_pen.forward(900)
    border_pen.right(90)
    border_pen.forward(700)
    border_pen.right(90)
border_pen.hideturtle()

# Title and Text
title_pen = turtle.Turtle()
title_pen.penup()
title_pen.hideturtle()
title_pen.color("white")
title_pen.goto(0, 360)
title_pen.write("Life Under the Sea", align="center", font=("Courier", 30, "bold"))

text_pen = turtle.Turtle()
text_pen.penup()
text_pen.hideturtle()
text_pen.color("lightgreen")
text_pen.goto(0, -370)
text_pen.write("Code with AP", align="center", font=("Courier", 18, "italic"))

# Fish class with enhanced movement
class Fish:
    def __init__(self, color, speed, size):
        self.body = turtle.Turtle()
        self.body.shape("triangle")
        self.body.color(color)
        self.body.shapesize(stretch_wid=size, stretch_len=size)  # Different sizes
        self.body.penup()
        self.body.speed(0)
        self.body.goto(random.randint(-400, 400), random.randint(-300, 300))
        self.body.setheading(random.randint(0, 360))
        self.speed = speed

    def move(self):
        self.body.forward(self.speed)
        # Boundary detection with bouncing
        if self.body.xcor() > 430 or self.body.xcor() < -430:
            self.body.right(180)
        if self.body.ycor() > 330 or self.body.ycor() < -330:
            self.body.right(180)

# Bubble class
class Bubble:
    def __init__(self):
        self.body = turtle.Turtle()
        self.body.shape("circle")
        self.body.color("white")
        self.body.shapesize(random.uniform(0.5, 1.5))
        self.body.penup()
        self.body.speed(0)
        self.body.goto(random.randint(-400, 400), random.randint(-350, -300))
        self.speed = random.uniform(0.5, 1.5)

    def rise(self):
        self.body.sety(self.body.ycor() + self.speed)
        # Respawn bubble at bottom when it reaches top
        if self.body.ycor() > 350:
            self.body.goto(random.randint(-400, 400), random.randint(-350, -300))

# Seaweed class with different variations
class Seaweed:
    def __init__(self, x, y, height, color):
        self.body = turtle.Turtle()
        self.body.color(color)
        self.body.penup()
        self.body.goto(x, y)
        self.body.pendown()
        self.body.speed(0)
        self.height = height
        self.draw_seaweed()

    def draw_seaweed(self):
        for _ in range(self.height):
            self.body.forward(20)
            self.body.right(30)
            self.body.forward(10)
            self.body.left(60)
            self.body.forward(10)
            self.body.right(30)

# Coral class (new element)
class Coral:
    def __init__(self, x, y, color):
        self.body = turtle.Turtle()
        self.body.shape("circle")
        self.body.color(color)
        self.body.penup()
        self.body.goto(x, y)
        self.body.shapesize(stretch_wid=2, stretch_len=3)

# Create corals
corals = [Coral(-300, -340, "pink"), Coral(250, -340, "purple"), Coral(50, -340, "red")]

# Sunken Treasure Chest class (new element)
class TreasureChest:
    def __init__(self, x, y):
        self.body = turtle.Turtle()
        self.body.shape("square")
        self.body.color("brown")
        self.body.shapesize(stretch_wid=2, stretch_len=3)
        self.body.penup()
        self.body.goto(x, y)

# Create treasure chest
treasure_chest = TreasureChest(-100, -330)

# Create seaweeds with varying heights
seaweeds = [Seaweed(-400, -350, 10, "green"), Seaweed(-300, -350, 12, "darkgreen"),
            Seaweed(-200, -350, 8, "lightgreen"), Seaweed(300, -350, 9, "green")]

# Create fishes with different colors and sizes
fishes = [Fish("orange", 2, 1), Fish("red", 2.5, 1.5), Fish("yellow", 3, 1), 
          Fish("blue", 2, 0.8), Fish("purple", 3.5, 1.2), Fish("cyan", 2.8, 1.3)]

# Create bubbles
bubbles = [Bubble() for _ in range(20)]

# Main loop for animation
while True:
    for fish in fishes:
        fish.move()

    for bubble in bubbles:
        bubble.rise()

    # Update screen for animation
    wn.update()
    time.sleep(0.017)  # Control the speed of the animation

# Close the turtle window on click
wn.mainloop()
