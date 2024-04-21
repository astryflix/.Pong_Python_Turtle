import turtle
import time
from ball import Ball
from paddle import Paddle

sc = turtle.Screen()
turtle.setup(width=800, height=600)
turtle.bgcolor('black')
sc.title("Pong")
sc.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

sc.listen()
sc.onkeypress(r_paddle.go_up, "Up")
sc.onkeypress(r_paddle.go_down, "Down")
sc.onkeypress(l_paddle.go_up, "w")
sc.onkeypress(l_paddle.go_down, "s")

# paddle location
# def r_paddle_loc():
#   ball.ycor() < r_paddle.pos() and ball.ycor() > r_paddle.pos() - 60
# r_paddle_loc = r_paddle.pos() and r_paddle.pos() - 60

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    sc.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # detect collision with paddle
    if abs(ball.xcor() - r_paddle.xcor()) < 15 and abs(ball.ycor() - r_paddle.ycor()) < 40:
        ball.bounce_paddle()
    if abs(ball.xcor() - l_paddle.xcor()) < 15 and abs(ball.ycor() - l_paddle.ycor()) < 40:
        ball.bounce_paddle()

sc.exitonclick()
