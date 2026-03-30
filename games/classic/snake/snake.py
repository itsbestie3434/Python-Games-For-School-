import turtle
import time
import random

# Game Setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0) # Turns off animations for custom updates

# Snake Head
head = turtle.Turtle("square")
head.color("black")
head.penup()

# Food
food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake Body
segments = []

# Directions
def go_up(): head.setheading(90)
def go_down(): head.setheading(270)
def go_left(): head.setheading(180)
def go_right(): head.setheading(0)

# Keyboard Controls
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Main Loop
while True:
    screen.update()
    
    # Check Food Collision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        new_segment = turtle.Turtle("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
    # Move Body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())
        
    head.forward(20)
    time.sleep(0.1)
