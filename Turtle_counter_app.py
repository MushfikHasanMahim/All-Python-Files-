import turtle as a
import time 
import random

t = a.Turtle()
a.bgcolor("#24252a")
a.speed(0)
a.penup()
a.goto(0, -200)
a.color("white")
a.goto(0, 0)
a.hideturtle()
i = 1
t.hideturtle()
while True:
    if i > 10:
        break
    a.bgcolor("#24252a") 
    t.color("white")
    t.write(i, font=("Arial", 40, "bold"), align="center")
    
    time.sleep(1)
    i += 1
    t.clear()
 
a.color("#fff")
a.bgcolor("#24252a")    
for i in range(100):
    a.color(random.choice(["#24252a", "green", "dodgerblue", "red", "yellow", "pink"]))
    a.speed(2)
    a.hideturtle()    
    a.write("Hello, Happy Birthday! ", align="center", font=("Arial", 17))
    time.sleep(.1)
    
time.sleep(10)
