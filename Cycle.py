import turtle

def draw_border():
    turtle.penup()
    turtle.goto(-300, 250)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("black")
    turtle.color("lightgray")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def draw_road():
    turtle.goto(-300, -150)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(150)
    turtle.end_fill()
    turtle.penup()

def draw_cycle():
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.pensize(3)
    turtle.color("black")

    # Draw wheels
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.circle(50)
    
    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.circle(50)

    # Draw frame
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.goto(0, 50)
    turtle.goto(100, -50)
    
    turtle.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.goto(-50, -50)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(50, -50)
    turtle.goto(-100, -50)
    turtle.penup()

def draw_title():
    turtle.goto(0, 300)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Python Turtle Graphics: Cycle", align="center", font=("Arial", 24, "bold"))
    turtle.penup()

def draw_text():
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Code by AP", align="center", font=("Arial", 18, "bold"))
    turtle.penup()

def add_3d_effects():
    # Wheels 3D Effect
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.color("darkgray")
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.circle(50, 180)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(100, -50)
    turtle.pendown()
    turtle.color("darkgray")
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.circle(50, 180)
    turtle.end_fill()
    turtle.penup()

def main():
    turtle.speed(0)
    turtle.hideturtle()

    draw_border()
    draw_road()
    draw_cycle()
    draw_title()
    draw_text()
    add_3d_effects()

    turtle.done()

if __name__ == "__main__":
    main()
