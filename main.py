import turtle
import random

MAX_sPEED = 1.5

def randSpeed():
    return round(random.uniform(-MAX_sPEED, MAX_sPEED), 2)

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=2000, height=1000)
window.tracer(0)

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=6, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-900, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=6, stretch_len=1)
paddle_2.penup()
paddle_2.goto(900, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = randSpeed()
ball.dy = randSpeed()

# functions
def move_paddle_1_up():
    y = paddle_1.ycor()
    y += 30
    paddle_1.sety(y)


def move_paddle_1_down():
    y = paddle_1.ycor()
    y -= 30
    paddle_1.sety(y)


def move_paddle_2_up():
    y = paddle_2.ycor()
    y += 30
    paddle_2.sety(y)


def move_paddle_2_down():
    y = paddle_2.ycor()
    y -= 30
    paddle_2.sety(y)


# key bindings
window.listen()
window.onkeypress(move_paddle_1_up, "w")
window.onkeypress(move_paddle_1_down, "s")
window.onkeypress(move_paddle_2_up, "Up")
window.onkeypress(move_paddle_2_down, "Down")


# game play loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() >= 490:
        ball.sety(490)
        ball.dy *= -1

    if ball.ycor() <= -490:
        ball.sety(-490)
        ball.dy *= -1

    if ball.xcor() >= 990:
        ball.goto(0,0)
        ball.dx = randSpeed()

    if ball.xcor() <= -990:
        ball.goto(0,0)
        ball.dx = randSpeed()

    # paddle hit
