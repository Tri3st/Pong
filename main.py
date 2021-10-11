from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  #collision wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #collision paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
    ball.bounce_x()

  #off the wall
  if ball.xcor() > 380:
    ball.center()
    #player 1 wins
    #score player 1 + 1
    scoreboad.l_point()
    
  if ball.xcor() < -380:
    ball.center()
    #player 2 wins
    #score player 2 + 1
    scoreboard.r_point()
  
  

screen.exitonclick()
