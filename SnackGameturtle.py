from turtle import*
import time


title("SnackGame")
bgcolor('#24241a')
tracer(0)
setup(600, 600)



# creating Head of the snack

HEAD = Turtle()
HEAD.speed(0)
HEAD.shape("circle")
HEAD.color("White")
HEAD.penup()
HEAD.goto(0, 100)
HEAD.direction = "stop"
HEAD.turtlesize(2)


# Moving Snack Head

def move():
    if HEAD.direction == 'up':
        y = HEAD.ycor()
        HEAD.sety(y + 20)
    elif HEAD.direction == 'down':
        y = HEAD.ycor()
        HEAD.sety(y - 20)
        
    elif HEAD.direction == 'left':
        x = HEAD.xcor()
        HEAD.setx(x + 20)
    elif HEAD.direction == 'right':
        x = HEAD.xcor()
        HEAD.setx(x - 20)
    else:
        pass    



# direction

def go_up():
    if HEAD.direction != "down":
        HEAD.direction = 'up'
    if HEAD.direction != "up":
        HEAD.direction = 'down'
    if HEAD.direction != "left":
        HEAD.direction = 'right'
    if HEAD.direction != "right":
        HEAD.direction = 'left'
    




# event loop

while True:
    update()
    move()
    time.sleep(0.1)

done()