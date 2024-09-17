import turtle

from datetime import datetime

turtle.bgcolor("black")
turtle.speed(0)
t = turtle.Turtle()
t.pensize(5)
t.pencolor("red")
print("\nProcess START: " + str(datetime.now()))

for x in range(10 ,750, 10):
    t.forward(x)
 
    t.right(91)

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))
    
print("Please close graphics window to end program.")

turtle.mainloop()
