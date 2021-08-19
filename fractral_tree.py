from tkinter import*


def fractral_tree(i):
	if i <= 10:
		return
	forward(i)
	left(30)
	fractral_tree(3*i/4)
	right(60)
	fractral_tree(3*i/4)
	left(30)
	backward(i)
	

fractral_tree(100)
	