# This is a youtube course, for a simple Pong game
# Was created in Python 3, but the creator says that doesnt really change o lot of things
# Let' get started
# All going really well, but I want more!! Lets make some changes
import turtle
import winsound


class Board():
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong by Course")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)
# All this command lines above give us the right setup for a window
# We choose its color, lengths and the title

# Work in progress...
    def flip(self, direction):
        pass

class Player:
    pass


# Score
score_a = 0
score_b = 0
special_count = 0
# During the beginning of the game, both paddles are at the borders of the board
paddle_a_center = False
paddle_b_center = False


# Board Creation
bg = Board()

#Paddle A
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
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375, 0)


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


def paddle_a_stop():
    y = paddle_a.ycor()
    paddle_a.sety(y)


def unbinding_a(x):
    bg.wn.onkeypress(paddle_a_stop, x)


def paddle_b_stop():
    y = paddle_b.ycor()
    paddle_b.sety(y)


def unbinding_b(x):
    bg.wn.onkeypress(paddle_b_stop, x)


def special_a():
    global special_count
    if special_count == 0:
        # global special_count
        special_count += 1
    if special_count == 3:
        paddle_b.goto(+50, paddle_b.ycor())
        global paddle_b_center
        paddle_b_center = True
        # global special_count
        special_count = 1
        print(special_count)
    if special_count == 2:
        bg.wn.onkeypress(paddle_b_up, "Left")
        bg.wn.onkeypress(paddle_b_down, "Right")
        unbinding_a("Up")
        unbinding_a("Down")
        # global special_count
        special_count += 1
        print(special_count)
    if special_count == 1:
        bg.wn.onkeypress(paddle_b_up, "Down")
        bg.wn.onkeypress(paddle_b_down, "Up")
        unbinding_a("Left")
        unbinding_a("Right")
        # global special_count
        special_count += 1
        print(special_count)


def get_special_count(x):
    x += 1
    return x


def special_b():
    global special_count
    if special_count == 0:
        # global special_count
        special_count += 1
    if special_count == 3:
        ball.goto(0, 0)
        # global special_count
        special_count = 1
        print(special_count)
    if special_count == 2:
        bg.wn.onkeypress(paddle_a_up, "s")
        bg.wn.onkeypress(paddle_a_down, "w")
        # global special_count
        special_count += 1
        print(special_count)
    if special_count == 1:
        bg.wn.onkeypress(paddle_a_up, "a")
        bg.wn.onkeypress(paddle_a_down, "d")
        # global special_count
        special_count += 1
        print(special_count)


# Keyboard binding / Inputs
bg.wn.listen()
bg.wn.onkeypress(paddle_a_up, "w")
bg.wn.onkeypress(paddle_a_down, "s")
bg.wn.onkeypress(paddle_b_up, "Up")
bg.wn.onkeypress(paddle_b_down, "Down")
# Special Attacks
bg.wn.onkeypress(special_a, "Tab")
bg.wn.onkeypress(special_b, "space")


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

# Main Game Loop
# My game doesnt have a star/stop botton yet
while True:
    bg.wn.update()

    # Ball movement
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
    if paddle_b_center:
        if ball.xcor() > 40 and (ball.ycor() < (paddle_b.ycor()+35) and (ball.ycor() > paddle_b.ycor()-35)):
            ball.setx(40)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if ball.xcor() < -350 and (ball.ycor() < (paddle_a.ycor()+35) and (ball.ycor() > paddle_a.ycor()-35)):
            ball.setx(-350)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    else:
        if ball.xcor() > 350 and (ball.ycor() < (paddle_b.ycor()+35) and (ball.ycor() > paddle_b.ycor()-35)):
            ball.setx(350)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if ball.xcor() < -350 and (ball.ycor() < (paddle_a.ycor()+35) and (ball.ycor() > paddle_a.ycor()-35)):
            ball.setx(-350)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if paddle_a_center:
        if ball.xcor() > 350 and (ball.ycor() < (paddle_b.ycor()+35) and (ball.ycor() > paddle_b.ycor()-35)):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if ball.xcor() < -40 and (ball.ycor() < (paddle_a.ycor()+35) and (ball.ycor() > paddle_a.ycor()-35)):
            ball.setx(-40)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    else:
        if ball.xcor() > 350 and (ball.ycor() < (paddle_b.ycor()+35) and (ball.ycor() > paddle_b.ycor()-35)):
            ball.setx(350)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if ball.xcor() < -350 and (ball.ycor() < (paddle_a.ycor()+35) and (ball.ycor() > paddle_a.ycor()-35)):
            ball.setx(-350)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)