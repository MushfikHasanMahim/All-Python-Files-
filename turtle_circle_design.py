from turtle import*


bgcolor('Black')
size = 200
speed(0)
pensize(15)
colours = ["Green", 'Orange', 'Yellow', 'DodgerBlue', 'Purple', 'Tomato']
j = 0
for i in range(size):
	if j > 5:
		j = 0
	color(colours[j])
	forward(i)
	left(50)
	j += 1


penup()
left(170)	
backward(500)
left(90)
forward(240)

color('white')
write('Programmed in Python Programming Language', font=('Terminal', 8, 'bold'))
done()