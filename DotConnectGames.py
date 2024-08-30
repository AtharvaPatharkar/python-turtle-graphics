import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Dot Connect Games")
screen.bgcolor("lightgrey")

# Set up the pen for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw 3D border
pen.penup()
pen.goto(-160, 160)
pen.pendown()
pen.color("black", "grey")
pen.begin_fill()
for _ in range(4):
    pen.forward(320)
    pen.right(90)
pen.end_fill()

# Draw inner 3D border
pen.penup()
pen.goto(-150, 150)
pen.pendown()
pen.color("white", "lightblue")
pen.begin_fill()
for _ in range(4):
    pen.forward(300)
    pen.right(90)
pen.end_fill()

# Set up the initial dot positions
dot_positions = []
rows, cols = 5, 5  # You can change this for a larger grid
spacing = 50  # Spacing between dots

# Function to draw dots with 3D effects
def draw_dots():
    for row in range(rows):
        for col in range(cols):
            x = col * spacing - (cols - 1) * spacing / 2
            y = row * spacing - (rows - 1) * spacing / 2
            dot_positions.append((x, y))
            pen.penup()
            pen.goto(x - 3, y - 3)
            pen.pendown()
            pen.dot(16, "darkblue")
            pen.penup()
            pen.goto(x, y)
            pen.dot(12, "blue")

# Initialize game variables
first_dot = None
second_dot = None
player = random.choice(["Player 1", "Player 2"])  # Random toss to decide first player
scores = {"Player 1": 0, "Player 2": 0}
round_number = 1
moves_left = (rows - 1) * (cols - 1) * 2  # Maximum number of moves
total_bonus_points = {"Player 1": 0, "Player 2": 0}

# Function to draw the title and creator text
def draw_title_and_creator():
    title_pen = turtle.Turtle()
    title_pen.hideturtle()
    title_pen.penup()
    title_pen.goto(0, 210)
    title_pen.color("darkblue")
    title_pen.write("Dot Connect Game", align="center", font=("Arial", 20, "bold"))

    creator_pen = turtle.Turtle()
    creator_pen.hideturtle()
    creator_pen.penup()
    creator_pen.goto(0, 190)
    creator_pen.color("darkred")
    creator_pen.write("Created by AP", align="center", font=("Arial", 12, "italic"))

# Function to display the current player, score, and moves
info_pen = turtle.Turtle()
info_pen.hideturtle()
info_pen.penup()
info_pen.goto(-150, 170)
info_pen.color("black")

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-150, 190)
score_pen.color("black")

moves_pen = turtle.Turtle()
moves_pen.hideturtle()
moves_pen.penup()
moves_pen.goto(50, 170)
moves_pen.color("black")

round_pen = turtle.Turtle()
round_pen.hideturtle()
round_pen.penup()
round_pen.goto(0, -200)
round_pen.color("darkblue")

# Function to update the display
def update_display():
    global moves_left
    info_pen.clear()
    if player == "Player 1":
        info_pen.color("darkgreen")
    else:
        info_pen.color("darkorange")
    info_pen.write(f"{player}'s Turn", font=("Arial", 12, "bold"))
    score_pen.clear()
    score_pen.write(f"Score - Player 1: {scores['Player 1']} | Player 2: {scores['Player 2']}", font=("Arial", 12, "bold"))
    moves_pen.clear()
    moves_pen.write(f"Moves Left: {moves_left}", font=("Arial", 12, "bold"))
    round_pen.clear()
    round_pen.write(f"Round {round_number}: {player}", align="center", font=("Arial", 14, "bold"))

# Function to display the winner and bonus points for a round
def display_round_winner():
    winner = "Player 1" if scores["Player 1"] > scores["Player 2"] else "Player 2"
    round_pen.goto(0, 180)
    round_pen.color("red")
    round_pen.write(f"Round Winner: {winner}!", align="center", font=("Arial", 18, "bold"))
    
    bonus_points = random.randint(5, 10) + 10  # Add 10 points to random bonus
    scores[winner] += bonus_points
    total_bonus_points[winner] += bonus_points
    
    round_pen.goto(0, 150)
    round_pen.write(f"Bonus Points: +{bonus_points}", align="center", font=("Arial", 14, "bold"))
    
# Function to reset the game for the next round
def reset_game():
    global first_dot, second_dot, player, moves_left, round_number
    pen.clear()
    draw_dots()
    first_dot = None
    second_dot = None
    player = random.choice(["Player 1", "Player 2"])  # Random toss for the next round
    moves_left = (rows - 1) * (cols - 1) * 2
    round_number += 1
    update_display()

# Function to display the final winner and end the game
def end_game():
    final_winner = "Player 1" if scores["Player 1"] > scores["Player 2"] else "Player 2"
    round_pen.goto(0, 100)
    round_pen.color("purple")
    round_pen.write(f"Final Winner: {final_winner}!", align="center", font=("Arial", 18, "bold"))
    round_pen.goto(0, 70)
    round_pen.write(f"Total Score - Player 1: {scores['Player 1']} | Player 2: {scores['Player 2']}", align="center", font=("Arial", 14, "bold"))
    round_pen.goto(0, 40)
    round_pen.write(f"Total Bonus Points - Player 1: {total_bonus_points['Player 1']} | Player 2: {total_bonus_points['Player 2']}", align="center", font=("Arial", 14, "bold"))
    
# Function to add a restart button
def restart_button(x, y):
    if -50 < x < 50 and -220 < y < -180:
        reset_game()

# Function to add an end game button
def end_game_button(x, y):
    if -50 < x < 50 and -240 < y < -200:
        end_game()

# Function to connect two dots
def connect_dots(x, y):
    global first_dot, second_dot, player, moves_left
    if moves_left == 0:
        return
    for dot in dot_positions:
        if abs(x - dot[0]) < 10 and abs(y - dot[1]) < 10:
            if first_dot is None:
                first_dot = dot
                pen.penup()
                pen.goto(dot[0], dot[1])
                pen.dot(12, "red")  # Change color to indicate selection
            else:
                second_dot = dot
                pen.penup()
                pen.goto(second_dot[0], second_dot[1])
                pen.dot(12, "red")
                pen.goto(first_dot[0], first_dot[1])
                pen.pendown()
                pen.width(3)
                pen.color("darkred")
                pen.goto(second_dot[0], second_dot[1])
                pen.width(1)
                first_dot = None
                second_dot = None
                scores[player] += 1
                moves_left -= 1
                if moves_left == 0:
                    display_round_winner()
                    pen.penup()
                    pen.goto(0, -220)
                    pen.pendown()
                    pen.color("black")
                    pen.write("Click here to Restart", align="center", font=("Arial", 12, "bold"))
                    screen.onclick(restart_button)
                    pen.penup()
                    pen.goto(0, -240)
                    pen.pendown()
                    pen.write("Click here to End Game", align="center", font=("Arial", 12, "bold"))
                    screen.onclick(end_game_button)
                    return
                if player == "Player 1":
                    player = "Player 2"
                else:
                    player = "Player 1"
                update_display()
            break

# Draw the title and creator text
draw_title_and_creator()
# Initial display update
update_display()
# Draw the initial grid of dots
draw_dots()

# Bind the click event to the connect_dots function
screen.onclick(connect_dots)

# Start the game loop
screen.mainloop()
