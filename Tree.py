from turtle import * 

speed(0)
left(90)

def fractral_tree(i):
    if i < 15:
        circle(4)
        shape("circle")
        return 
       
    pensize(i // 12)    
    forward(i)       
    left(30)  
    fractral_tree(3 * i // 4)
    right(60)
    fractral_tree(3 * i // 4)
    left(30)
    backward(i)
    

fractral_tree(200)

done()



