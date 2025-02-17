import turtle
import datetime
import math


# Set up the screen
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("#b5c4a0")
screen.setup(width=800, height=600)

# Draw the clock face with a border and 3D effect
clock_face = turtle.Turtle()
clock_face.speed(0)
clock_face.penup()
clock_face.goto(0, -210)
clock_face.pendown()
clock_face.fillcolor("#FFFFFF")  # White clock face
clock_face.begin_fill()
clock_face.circle(210)
clock_face.end_fill()

# Draw the outer border with 3D effect
border = turtle.Turtle()
border.speed(0)
border.penup()
border.goto(0, -220)
border.pendown()
border.color("#000000")  # Black border
border.width(5)
border.circle(220)

# 3D effect for the border
border.penup()
border.goto(0, -235)
border.pendown()
border.color("#A9A9A9")  # Dark grey for 3D effect
border.width(7)
border.circle(235)

# Draw the numbers 0 to 11 on the clock face
number_turtle = turtle.Turtle()
number_turtle.speed(0)
number_turtle.penup()
radius = 180  # Distance from the center of the clock face

for i in range(12):
    angle = math.radians(90 - i * 30)  # Calculate the angle for each number
    x = radius * math.cos(angle)  # Calculate the x position
    y = radius * math.sin(angle)  # Calculate the y position
    number_turtle.goto(x, y)
    number_turtle.write(str(i), align="center", font=("Arial", 24, "bold"))

# Draw the numbers 0 to 59 on the second border
second_number_turtle = turtle.Turtle()
second_number_turtle.speed(0)
second_number_turtle.penup()
second_radius = 235  # Distance from the center of the clock face for the second border numbers

for i in range(60):
    angle = math.radians(90 - i * 6)  # Calculate the angle for each number
    x = second_radius * math.cos(angle)  # Calculate the x position
    y = second_radius * math.sin(angle)  # Calculate the y position
    second_number_turtle.goto(x, y)
    second_number_turtle.write(str(i), align="center", font=("Arial", 8, "normal"))

# Draw the road and car (same as before)
road = turtle.Turtle()
road.speed(0)
road.penup()
road.goto(-400, -280)
road.pendown()
road.color("#4B4B4B")  # Dark gray road
road.begin_fill()
road.forward(800)
road.right(90)
road.forward(60)
road.right(90)
road.forward(800)
road.right(90)
road.forward(60)
road.end_fill()

car = turtle.Turtle()
car.speed(0)
car.penup()
car.goto(-300, -250)
car.pendown()
car.color("#FF0000")  # Red car
car.begin_fill()
car.forward(100)  # Car body length
car.right(90)
car.forward(50)  # Car body width
car.right(90)
car.forward(100)
car.right(90)
car.forward(50)
car.end_fill()

# Draw car wheels
car_wheel1 = turtle.Turtle()
car_wheel1.speed(0)
car_wheel1.penup()
car_wheel1.goto(-270, -260)
car_wheel1.pendown()
car_wheel1.color("#000000")  # Black wheels
car_wheel1.begin_fill()
car_wheel1.circle(10)
car_wheel1.end_fill()

car_wheel2 = turtle.Turtle()
car_wheel2.speed(0)
car_wheel2.penup()
car_wheel2.goto(-230, -260)
car_wheel2.pendown()
car_wheel2.color("#000000")  # Black wheels
car_wheel2.begin_fill()
car_wheel2.circle(10)
car_wheel2.end_fill()

# Make custom shapes for clock hands - Currently Lines
turtle.register_shape("hour_hand", ((-4, -5), (4, -5), (2, 150), (-2, 150)))
turtle.register_shape("minute_hand", ((-2, -5), (2, -5), (1, 200), (-1, 200)))
turtle.register_shape("second_hand", ((-1, -5), (1, -5), (0.5, 220), (-0.5, 220)))

# Creating clock hands
hands = []
for shape, color in [("hour_hand", "black"), ("minute_hand", "blue"), ("second_hand", "red")]:
    hand = turtle.Turtle()
    hand.shape(shape)
    hand.color(color)
    hands.append(hand)

# Function to update the position of clock hands
def update_clock_hands():
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Calculates the angles based on the current time
    angles = [
        (hour + minute / 60) * 360 / 12,
        (minute + second / 60) * 360 / 60,
        (second + now.microsecond / 1000000) * 360 / 60
    ]

    # Align the clock hands on the clock face by converting the clock angles to turtle angles.
    for hand, angle in zip(hands, angles):
        hand.setheading(90 - angle)

# Create a digital time display over the clock
digital_time_display = turtle.Turtle()
digital_time_display.speed(0)
digital_time_display.penup()
digital_time_display.goto(0, 280)
digital_time_display.pendown()
digital_time_display.hideturtle()

# Function to update digital time - gets current time, clears previous screen, write new time 
def update_digital_time():
    now = datetime.datetime.now()
    digital_time_display.clear()
    digital_time_display.color("black")
    digital_time_display.write(now.strftime("%H:%M:%S"), align="center", font=("Arial", 36, "bold"))

# Function to update the clock and digital time
def update_clock():
    update_clock_hands()
    update_digital_time()
    screen.update()
    screen.ontimer(update_clock, 1000)

# Add text below the clock
text_display = turtle.Turtle()
text_display.speed(0)
text_display.penup()
text_display.goto(0, -270)
text_display.pendown()
text_display.hideturtle()
text_display.color("black")
text_display.write("Analog Clock", align="center", font=("Arial", 24, "italic"))

# Start the clock
update_clock()

turtle.hideturtle()

turtle.done()
