import turtle
import random
import time

delay = 0.1
sc = 0  # Score
hs = 0  # Highest_Score

# Creating a body of a Snake
bodies = []

# Creating a Screen
s = turtle.Screen()
s.title("Snake Game")          # Title
s.bgcolor("lightpink")        # Colour
s.setup(width=600, height=600)  # Size of the screen

# Creating a head
head = turtle.Turtle()
head.speed(0)           # Speed function
head.shape("circle")    # Shape function
head.color("blue")
head.fillcolor("red")
head.penup()
head.ht()               # (Hiding Turtle) For hiding a turtle
head.goto(0, 0)
head.st()               # (Showing Turtle) For showing the turtle
head.direction = 'stop'

# Creating a food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()               # (Hiding Turtle) For hiding a turtle
food.goto(0, 100)
food.st()               # (Showing Turtle) For showing the turtle

# Creating a score board
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score: 0   -   Highest Score: 0", align="left", font=("Courier", 12, "normal"))

# Creating function for moving in all direction
def moveUp():
    if head.direction != "down":      # !=  not equal to
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()          # Here Y is coordinate
        head.sety(y + 20)

    if head.direction == "left":
        x = head.xcor()          # Here X is coordinate
        head.setx(x - 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling for moving snake
s.listen()                   # Function
s.onkey(moveUp, "Up")        # ^ arrow Up
s.onkey(moveDown, "Down")    # arrow Down
s.onkey(moveLeft, "Left")    # < arrow Left
s.onkey(moveRight, "Right")  # > arrow Right
s.onkey(moveStop, "space")   # Stop - Space

# Main loop
while True:
    s.update()               # To update the screen

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = "stop"

        # Hide bodies
        for body in bodies:
            body.ht()

        bodies.clear()
        sc = 0
        delay = 0.1
        sb.clear()
        sb.write("Score: {}  |  Highest Score: {}".format(sc, hs), align="left", font=("Courier", 12, "normal"))

    # Check collision with food
    if head.distance(food) < 20:           # Distance from food
        x = random.randint(-270, 270)      # Random Library
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Increase the body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)             # Append new body in the list

        sc += 10                        # Increase the score
        delay -= 0.001                  # Increase the speed

        if sc > hs:
            hs = sc                     # Update highest score
        sb.clear()
        sb.write("Score: {}  |   Highest Score: {}".format(sc, hs), align="left", font=("Courier", 12, "normal"))

    # Move Snake's body
    for i in range(len(bodies) - 1, 0, -1):     # Length of Snake's body
        x = bodies[i - 1].xcor()                # Coordinate X
        y = bodies[i - 1].ycor()                # Coordinate Y
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with self body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)        # Sleep (1) means Sleep True
            head.goto(0, 0)
            head.direction = "stop"

            # Hide bodies
            for b in bodies:
                b.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {}  |  Highest Score: {}".format(sc, hs), align="left", font=("Courier", 12, "normal"))

    time.sleep(delay)
s.mainloop()
