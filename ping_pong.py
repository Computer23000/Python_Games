import turtle

## creating the window
window=turtle.Screen()
window.title('Ping Pong')
window.bgcolor('black')
window.setup(width=800,height=600)
window.tracer(0)

#score variables
score_a=0
score_b=0

# left paddle exist and start place
left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350,0)

# right paddle exist and start place
right_paddle=turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350,0)

# Ball exist and position
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx=3.5
ball.dy=3.5

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0 Player B: 0', align='center', font=('Courier', 24 , 'normal'))

### define functions for paddle movement
# left paddle up
def left_paddle_up():
    y=left_paddle.ycor()
    y+=20
    left_paddle.sety(y)

# left paddle down
def left_paddle_down():
    y=left_paddle.ycor()
    y-=20
    left_paddle.sety(y)

# right paddle up
def right_paddle_up():
    y=right_paddle.ycor()
    y+=20
    right_paddle.sety(y)

# right paddle down
def right_paddle_down():
    y=right_paddle.ycor()
    y-=20
    right_paddle.sety(y)

# keyboard binding for paddle movement
window.listen()
window.onkeypress(left_paddle_up,'w')
window.onkeypress(left_paddle_down,'s')
window.onkeypress(right_paddle_up,'Up')
window.onkeypress(right_paddle_down,'Down')


# main game loop
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #check border
    #top border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    #bottom border
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    #right border
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        #score keeping
        score_a += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24 , 'normal'))

    # left border
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        #score keeping
        score_b += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24 , 'normal'))

    #paddle and ball collisions
    #right paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    # left paddle and ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
