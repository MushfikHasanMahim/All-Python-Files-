from tkinter import*


class Calculator:
	Font = ('Arial', 10, 'bold')
	Str = ''
	digits = {
		1:[0, 0],
		2:[0, 1], 
		3:[0, 2],
		4:[1, 0],
		5:[1, 1],
		6:[1, 2],
		7:[2, 0],
		8:[2, 1],
		9:[2, 2],
		0:[3, 0]
	}
	
	action_btns = {
		'+' : [0, 3],
		'-' : [1, 3],
		'*' : [2, 3],
		'/' : [3, 3]
	}
	
	def __init__(self):
		self.app = Tk()
		self.app.configure(bg='#656565')
		self.label = self.create_label()
		self.entry_label = self.create_entry()
		
		self.frame = self.create_frame()

	
	def button_press(self, x):
		Calculator.Str += str(x)
		self.app.entry.config(text=self.Str)
		
		
	def create_label(self):
		self.app.label = Label(bg='#656565', fg='black', text='Claculator',font=('Times New Roman', 20, 'bold'), pady=270)
		return self.app.label.pack()

	
	def create_frame(self):
		self.app.frame = Frame()
		for btn, pos in self.digits.items():
			button = Button(self.app.frame, borderwidth=0,text=str(btn), bg='lightgray', height=2, width=10, command= lambda x=btn:self.button_press(x))
			button.grid(row=pos[0], column=pos[1], sticky=NSEW)
		return self.app.frame.pack(fill=BOTH, expand=True)
	
	
	
	def create_entry(self):
		self.app.entry = Label(anchor='e', font=self.Font, height=10, pady=190)
		return self.app.entry.pack(fill=BOTH, expand=True)
		
				
	def run(self):
		return self.app.mainloop()
	
		
	
if __name__ == '__main__':
	App = Calculator()
	App.run()