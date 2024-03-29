#Free and open source.
#Jonathan Steadman.
#With help from https://almettkidscoding.github.io/basics/pong_game/
#End of life: 13th of August 2024.
#import turtle
import turtle
import tkinter
#Setting up the score
#Playsound will allow me to add some sound effects. 
from playsound import playsound

score1 = 0
score2 = 0
#Making the screen for the python game.
screen = turtle.Screen()
screen.title("Basic Ping Pong Game 4.0! By Jonathan Steadman!")
screen.bgcolor("pink")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)
#Icon image... :)
img = tkinter.Image("photo", file="pingpong.png")
turtle._Screen._root.iconphoto(True, img)

#Creating the paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("green")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

#Creating the paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("purple")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

#Creating the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1
#Creating the score.
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player one: 0 Player two: 0", align="center", font=("Ubuntu", 25))

#Controls for paddle one
#----------------------------
#The paddle for player one will move up
def paddle1_up():
    y = paddle1.ycor()
    y += 60
    paddle1.sety(y)
#The paddle will move down
def paddle1_down():
    y = paddle1.ycor()
    y -= 60
    paddle1.sety(y)
#------------------------------
#Controls for paddle two.
def paddle2_up():
    y = paddle2.ycor()
    y += 60
    paddle2.sety(y)
def paddle2_down():
    y = paddle2.ycor()
    y -= 60
    paddle2.sety(y)

#Keybpard binding.
screen.listen()
screen.onkeypress(paddle1_up, "w")
screen.onkeypress(paddle1_down, "s")
screen.onkeypress(paddle2_up, "Up")
screen.onkeypress(paddle2_down, "Down")

#Workflow
while True:
    screen.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    #left and right
    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
        score1 += 1
        pen.clear()

        pen.write("Player one: {} Player two: {}".format(score1, score2), align="center", font=("Ubuntu", 25))
        #Why add block = false.
        #When the sound is played the game freeze but this will stop it from freezing the game. :)
        playsound('sounds/mixkit-light-impact-on-the-ground-2070.wav', block=False)

    if ball.xcor() > 380:
        if score2  <0:
            score2 = 0
        elif score2 >0:
            score2 -= 1
        playsound('sounds/cheer.mp3', block=False)

        pen.clear()
        pen.write("Player one: {} Player two: {}".format(score1, score2), align="center", font=("Ubuntu", 25))
        ball.goto(0, 0)
        ball.dx *= -1



    if ball.xcor() < -380:
        if score1 <0:
            score1 = 0
        elif score1 > 0:
            score1 -= 1
        #score1 -= 1
        playsound('sounds/cheer.mp3', block=False)

        pen.clear()
        pen.write("Player one: {} Player two: {}".format(score1, score2), align="center", font=("Ubuntu", 25))
        ball.goto(0, 0)
        ball.dx *= -1
    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
        score2 += 1
        pen.clear()

        pen.write("Player one: {} Player two: {}".format(score1, score2), align="center", font=("Ubuntu", 25, "normal"))
        playsound('sounds/mixkit-light-impact-on-the-ground-2070.wav', block=False)


    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

screen.mainloop()