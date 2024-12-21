import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System")

# Function to draw a planet
def draw_planet(name, color, distance, size):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.penup()
    planet.goto(distance, 0)
    planet.pendown()
    planet.shapesize(size)
    planet.write(name, align="center", font=("Arial", 10, "normal"))
    return planet

# Draw the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(0, 0)
sun.pendown()
sun.shapesize(4)  # Size of the Sun
sun.write("Sun", align="center", font=("Arial", 14, "bold"))

# Create planets
planets = [
    ("Mercury", "gray", 50, 0.5),
    ("Venus", "yellow", 100, 0.8),
    ("Earth", "blue", 150, 1),
    ("Mars", "red", 200, 0.6),
    ("Jupiter", "orange", 300, 2),
    ("Saturn", "gold", 400, 1.8),
    ("Uranus", "light blue", 500, 1.5),
    ("Neptune", "blue", 600, 1.5),
]

# Draw planets
for name, color, distance, size in planets:
    draw_planet(name, color, distance, size)

# Keep the window open
screen.mainloop()
