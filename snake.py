
import turtle
import time
import random

delay = 0.1

#Score
score: int = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("white")
wn.setup(width=600,height=600)
wn.tracer(0)

#Snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,100)

segments = []

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align="center", font=("Arial", 26, "normal"))

#Fuctions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
def reset():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    global score
    score = 0
    pen.clear()
    pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Arial", 26, "normal"))
    global delay
    delay = 0.1

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()


#keyboard bindings

wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")


#main game loop

while True:
    wn.update()

    #collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset()


    #collision with food

    if head.distance(food) < 20:

        #move the food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #add a tail to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorter the delay
        delay -= 0.001

        #increase the score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Arial", 26, "normal"))
    #move the end segments first in revers order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

     #move segment 0
    if len(segments) > 0:
         x = head.xcor()
         y = head.ycor()
         segments[0].goto(x, y)



    move()

    # head collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            reset()


    time.sleep(delay)

wn.mainloop()



