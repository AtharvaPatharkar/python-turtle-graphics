import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.bgcolor("#f1c2a5")  # Background color
screen.setup(width=600, height=600)

# Draw grid
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw grid with 3D effect
def draw_grid():
    # Draw grid squares with 3D effect
    for x in [-200, 0, 200]:
        for y in [200, 0, -200]:
            # Draw shadow for 3D effect
            pen.color("gray")
            pen.penup()
            pen.goto(x - 105, y + 95)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(210)
                pen.right(90)
            pen.end_fill()

            # Draw main box with color
            pen.color("black", "#e3a27b")  # Change fill color here
            pen.penup()
            pen.goto(x - 100, y + 100)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(200)
                pen.right(90)
            pen.end_fill()

    # Draw grid lines
    pen.color("white")
    pen.pensize(10)
    
    # Vertical lines
    pen.penup()
    pen.goto(-100, 300)
    pen.pendown()
    pen.goto(-100, -300)

    pen.penup()
    pen.goto(100, 300)
    pen.pendown()
    pen.goto(100, -300)

    # Horizontal lines
    pen.penup()
    pen.goto(-300, 100)
    pen.pendown()
    pen.goto(300, 100)

    pen.penup()
    pen.goto(-300, -100)
    pen.pendown()
    pen.goto(300, -100)

draw_grid()

def text():
    pen.color("black")
    pen.up()
    pen.goto(-125, -385)
    pen.down()
    pen.write("Restart", align="center", font=("Arial", 18, "bold"), )

def add_signature():
    pen.color("black")
    pen.penup()
    pen.goto(-350, 300)  # Adjust the position as needed
    pen.pendown()
    pen.write("Code by AP", align="left", font=("Comic Sans MS", 32, "italic"))
    pen.penup()
    pen.goto(150, 300)  # Adjust the position as needed
    pen.pendown()
    pen.write("Enjoy the Game!", align="left", font=("Comic Sans MS", 16, "italic"))

# Initialize board and player variables
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

def draw_x(x, y):
    pen.color("red")
    pen.pensize(8)
    pen.penup()
    pen.goto(x - 60, y + 60)
    pen.pendown()
    pen.goto(x + 60, y - 60)
    pen.penup()
    pen.goto(x + 60, y + 60)
    pen.pendown()
    pen.goto(x - 60, y - 60)

def draw_o(x, y):
    pen.color("blue")
    pen.pensize(8)
    pen.penup()
    pen.goto(x, y - 60)
    pen.pendown()
    pen.circle(60)

def check_winner():
    global game_over
    winner = None

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            winner = board[i][0]
            pen.penup()
            pen.goto(-300, 200 - i * 200)
            pen.pendown()
            pen.goto(300, 200 - i * 200)
            game_over = True

        if board[0][i] == board[1][i] == board[2][i] != "":
            winner = board[0][i]
            pen.penup()
            pen.goto(-200 + i * 200, 300)
            pen.pendown()
            pen.goto(-200 + i * 200, -300)
            game_over = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
        pen.penup()
        pen.goto(-300, 300)
        pen.pendown()
        pen.goto(300, -300)
        game_over = True

    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]
        pen.penup()
        pen.goto(300, 300)
        pen.pendown()
        pen.goto(-300, -300)
        game_over = True

    # Check for a tie
    if all(board[row][col] != "" for row in range(3) for col in range(3)) and not winner:
        winner = "None"
        game_over = True

    # Display the winner
    if game_over:
        display_winner(winner)

def display_winner(winner):
    pen.penup()
    pen.goto(0, -350)
    pen.pendown()
    pen.color("purple")
    pen.write(f"{winner} wins!" if winner != "None" else "It's a tie!", align="center", font=("Arial", 24, "bold"))

def restart_game():
    global board, current_player, game_over
    pen.clear()
    draw_grid()
    add_signature()
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

def click_handler(x, y):
    global current_player
    if game_over:
        return

    row = int((300 - y) // 200)
    col = int((x + 300) // 200)

    if board[row][col] == "":
        board[row][col] = current_player
        if current_player == "X":
            draw_x(-200 + col * 200, 200 - row * 200)
            current_player = "O"
        else:
            draw_o(-200 + col * 200, 200 - row * 200)
            current_player = "X"
        
        check_winner()

# Add a restart button
button = turtle.Turtle()
button.shape("square")
button.color("green")
button.shapesize(stretch_wid=2, stretch_len=6)
button.penup()
button.goto(0, -375)
text()
add_signature()

def button_click(x, y):
    if -60 <= x <= 60 and -390 <= y <= -360:
        restart_game()
        text()

# Link the button click to the handler
screen.onclick(click_handler)
button.onclick(button_click)

turtle.done()
