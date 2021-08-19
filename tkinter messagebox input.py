from tkinter import*
from tkinter.simpledialog import askstring as i
from tkinter.filedialog import messagebox as o


def wish():
	App = Tk()
	def input():
		name = i('Input', 'What\'s your name ')
		o.showinfo('Output', f'Hello, {name}')
	button = Button(text='Click', command=input)
	button.pack()
	App.mainloop()


wish()