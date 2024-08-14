import turtle

# Set the background color
turtle.bgcolor("#01c4f5")

s = turtle.getscreen()
t = turtle.Turtle()

# Function to draw a 3D border
def draw_3d_border():
    border_turtle = turtle.Turtle()
    
    # Darker shade for the outer border
    border_turtle.penup()
    border_turtle.goto(-320, 320)  # Starting position of the outer border
    border_turtle.pendown()
    border_turtle.pensize(10)
    border_turtle.pencolor("#0a0a0a")  # Dark grey color for 3D effect
    
    for _ in range(4):
        border_turtle.forward(640)
        border_turtle.right(90)
    
    # Lighter shade for the inner border
    border_turtle.penup()
    border_turtle.goto(-310, 310)  # Starting position of the inner border
    border_turtle.pendown()
    border_turtle.pensize(5)
    border_turtle.pencolor("#b0b0b0")  # Light grey color for 3D effect
    
    for _ in range(4):
        border_turtle.forward(620)
        border_turtle.right(90)
    
    border_turtle.hideturtle()

def hulk():
    t.pensize(20)
    t.fillcolor("Red")
    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    t.right(180)
    t.circle(100, -180)

    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()

    t.right(240)
    t.circle(50, -70)

    t.end_fill()

def glass():
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor('skyblue')
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()

def bagpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor("Red")
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()



def writes():
    t.penup()
    t.goto(-300,-300)
    t.pendown()
    t.color("white")
    t.pensize(10)
    t.write("Code with AP", font=("Arial Rounded MT Bold", 32, "bold"))







# Draw the 3D border first
draw_3d_border()

# Draw the hulk, glass, and backpack
hulk()
glass()
bagpack()

writes()

turtle.done()
