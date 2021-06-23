# This is a youtube course, for a simple Pong game
# Was created in Python 3, but the creator says that dont really change o lot of things
# Let' get started

import turtle
import winsound


# All this command lines above give us the right setup for a window
# We choose its color, lengths and the title
wn = turtle.Screen()
wn.title("Pong by Course")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-375, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+375, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
# Speed in the window, based on the number of pixels
ball.dx = 0.15 # 2 pixels
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0) # Animation Speed
pen.color("yellow")
pen.penup()
pen.hideturtle() # Will hide this object, we'll show the text that who will create
pen.goto(0, 250)
pen.write(f"Player A: {score_a}  |  Player B: {score_b}", align="center", font=("Courier", 22, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

# Keyboard binding / Inputs
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
#
while True:
    wn.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision and Border checking
    # Border Checks for upper bound
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # Border Checks for lower bound
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # Border Checks for right bound
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player A: {score_a}  |  Player B: {score_b}", align="center", font=("Courier", 22, "normal"))
    # Border Checks for left bound
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear() # This is a very quickly function, without being noticed by the human eye
        pen.write(f"Player A: {score_a}  |  Player B: {score_b}", align="center", font=("Courier", 22, "normal"))
    # Checking collision with the paddle
    if ball.xcor() > 350 and (ball.ycor() < (paddle_b.ycor()+35) and (ball.ycor() > paddle_b.ycor()-35)):
        ball.setx(350)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() < -350 and (ball.ycor() < (paddle_a.ycor()+35) and (ball.ycor() > paddle_a.ycor()-35)):
        ball.setx(-350)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)