import turtle

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
paddle_1.shapesize(stretch_wid=2, stretch_len=4)
paddle_1.penup()
paddle_1.goto(-1950, 0)

#Paddle 2


# game play loop
while True:
    window.update()