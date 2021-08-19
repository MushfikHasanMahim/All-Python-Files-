from turtle import*
from time import sleep


ht()
setup(width=20, height=20)
bgpic('frog.gif')
sleep(2)
def c():
    clear()
c()
speed(0)
title('Turtle example')
bgcolor("#101010")
color('#333')

a, b = 0, 0

while b!=180:
    forward(a)
    left(b)
    a += 3
    b += 1
    

penup() 
done()