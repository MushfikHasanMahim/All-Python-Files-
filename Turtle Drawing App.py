from turtle import*
from random import choice
import time


# intro()


t = Turtle()
t.speed(0)
t.shape('turtle')
t.shapesize(30)
t.setheading(90)

p = Turtle()
p.speed(0)
p.penup()
p.goto(0, -800)
p.hideturtle()
p.write("Turtle App\nMade by Mushfik Hasan Mahim", align="center", font=("Arial", 10))
for j in range(20):
    t.color(choice(["#24252a", "green", "dodgerblue", "red", "yellow", "pink"]))
    time.sleep(0.1)
p.clear()   
t.hideturtle()     
t.clear()
    
    
    
    
    
   





drawer = Turtle()
drawer.color("white")
drawer.speed(0)
drawer.showturtle()
drawer.shape("arrow")

def create_move_btns():  
    b1 = Turtle()
    b1.speed(0)
    b1.penup()
    b1.showturtle()
    b1.shapesize(3)
    b1.shape("circle")
    b1.fillcolor("yellow")
    b1.color("yellow")
    b1.onclick(up)
    b1.goto(0,-850)
    b1.write("", align="center", font=("Arial", 10, "bold"))
    
    
    b2 = Turtle()
    b2.speed(0)
    b2.penup()
    b2.showturtle()
    b2.shape("circle")
    b2.shapesize(3)
    b2.fillcolor("tomato")
    b2.color("tomato")
    b2.goto(0,-1050)
    b2.write("", align="center", font=("Arial", 10, "bold"))
    b2.onclick(down)
    
    
    
    b3 = Turtle()
    b3.speed(0)
    b3.penup()
    b3.showturtle()
    b3.shapesize(3)
    b3.fillcolor("dodgerblue")
    b3.color("dodgerblue")
    b3.shape("circle")
    b3.goto(-100,-950)
    b3.write("", align="center", font=("Arial", 10, "bold"))
    b3.onclick(left)
    
    b4 = Turtle()
    b4.speed(0)
    b4.penup()
    b4.showturtle()
    b4.shapesize(3)
    b4.shape("circle")
    b4.fillcolor("green")
    b4.color("green")
    b4.goto(100,-950)
    b4.write("", align="center", font=("Arial", 10, "bold"))
    b4.onclick(right)

def left(x, y):
    drawer.setheading(180)
    drawer.forward(100)
    
def right(x, y):
    drawer.setheading(0)
    drawer.forward(100)
    
def up(x, y):
    drawer.setheading(90)
    drawer.forward(100)
    
def down(x, y):
    drawer.setheading(270)
    drawer.forward(100)


create_move_btns() 
#while True:
#    #c = textinput("Input", " Direction (up / down / left / right) : ")
#    if c == "u":
#        up()
#    elif c == "d":
#        down()
#    elif c == "l":
#        left()
#    elif c == "r":
#        right()
#    
    
 

app = Screen()
app.setup(500, 500)
app.bgcolor("#24252a")
  
    
app.mainloop()
