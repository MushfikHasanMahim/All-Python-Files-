from tkinter import*


class Calculator():
	var = None
	var2 = None
	bgcolor="#072833"
	label = None
	TEXT = ''
	digits = {
	
		"0":(4, 0),
		"1":(1, 0),
		"2":(1, 1),
		"3":(1, 2),
		"4":(2, 0),
		"5":(2, 1),
		"6":(2, 2),
		"7":(3, 0),
		"8":(3, 1),
		"9":(3, 2),
		".":(4, 1)
		
		
	
	}
	
	spbtn = {
	    '\u00D7':'*',
	    '\u00F7':'/'
	}
	action_btns = {
		
		"+":(1, 3),
		"-":(2, 3),
		"\u00D7":(3, 3),
		"\u00F7":(4, 3),
		"%":(0, 3)
		
	}
	
	
	def __init__(self):
		self.app = Tk()
		self.create_window()
	
	def create_window(self):
		self.app.config(bg='black')
		
		# create label for title
	
		label = Label(self.app, text="Calculator", fg="#ffffff",  font=("Courier",20 ), bg=self.bgcolor)
		label.pack(fill=BOTH, expand=True)
		
		# create frame
		
		frame = Frame(self.app, bg=self.bgcolor, padx=50, pady=50)
		frame.pack(fill=BOTH)
		
		# create StringVariable
		
		# small 
		
		smallvar = StringVar()
		
		# big input
		strvar = StringVar()		
		
    	# creating small_label
		
		small_label = Label(frame, textvariable=smallvar, bg=self.bgcolor, fg="#ffffff", font=('Arial', 10, 'bold'), anchor='e', padx = 20, pady=150)
		small_label.pack(expand=True, fill=BOTH)
		
		smallvar.set("0")
		
		# create label for input()
		
		input_label = Label(frame, textvariable = strvar, bg=self.bgcolor, fg="#ffffff", font=("Arial", 30), height=1, anchor="e" )
		input_label.pack(fill=BOTH, expand=True)
		
		self.label = input_label
		
		# addaing 0
		
		strvar.set('0')
		
		# Adding Buttons 
		frame2 = Frame(bg=self.bgcolor)
		frame2.pack()
		for btn, pos in self.digits.items():
			digits_button = Button(frame2, text=btn, borderwidth=0,bg=self.bgcolor,fg="#e6f1f2", font=("Arial", 18, 'bold'), highlightthickness=0, command=lambda x=btn: self.on_press(x))
			digits_button.grid(row=pos[0], column=pos[1], sticky=NSEW, padx=60,  pady=40)
		
		# actions_buttons
		for btn, pos in self.action_btns.items():
			act_button = Button(frame2, text=btn,bg=self.bgcolor, borderwidth=0, font=("Arial", 18, 'bold'), fg="#e6f1f2", highlightthickness=0, command=lambda x=btn:self.on_press(x))
			act_button.grid(row=pos[0], column=pos[1], sticky=NSEW, padx=40,  pady=40)
			
		# Equal buttons
		eql_button = Button(frame2, text="=",bg="#020c14", borderwidth=0, font=("Arial", 18, 'bold'), fg="#e6f1f2", highlightthickness=0, command=self.result)
		eql_button.grid(row=4, column=2, sticky=NSEW, padx=60,  pady=40)
		
		
		# back button => \u232b
		
		back_button = Button(frame2, text="\u232b",bg=self.bgcolor, borderwidth=0, font=("Arial", 12, 'bold'), fg="#e6f1f2", highlightthickness=0, command=self.back)
		back_button.grid(row=0, column=2, sticky=NSEW, padx=60,  pady=40)
		
		# clear button 
		back_button = Button(frame2, text="C",bg=self.bgcolor, borderwidth=0, font=("Arial", 18, 'bold'), fg="#e6f1f2", highlightthickness=0, command=self.clear)
		back_button.grid(row=0, column=0, sticky=NSEW, padx=60,  pady=40)
		
		# square()
		
		sqrbtn = Button(frame2, text="x\u00B2",bg=self.bgcolor, borderwidth=0, font=("Arial", 18, 'bold'), fg="#e6f1f2", highlightthickness=0, command=self.square)
		sqrbtn.grid(row=0, column=1, sticky=NSEW, padx=60,  pady=40)
		self.var = strvar
		self.var2 = smallvar
	
	# on_press 
		
	def on_press(self, n):
		self.TEXT += n
		self.var.set(self.TEXT)
	
					
			
	def run(self):
		return self.app.mainloop()
	
	def result(self):
	    try:
	        self.var2.set(self.TEXT)
	        output = ''
	        for i in self.TEXT:
	            output += self.spbtn.get(i, i)
	            
	            
	        self.TEXT = str(eval(output))
	        if len(list(self.TEXT)) >= 10:
	            self.label.config(font=("Arial", 10))
	            
	            self.var.set(self.TEXT)

	        else:
	            self.label.config(font=("Arial", 30))
	            self.var.set(self.TEXT)
	        
	    except ZeroDivisionError:
	        self.var2.set("Can't Devide by 0 ")
	        self.var.set('Error')
	        self.TEXT = ""
	    except:
	        self.var.set("Error")
	        self.TEXT = ""
	# clear()        
	def clear(self):
	        self.var.set('')
	        self.TEXT = ''
	        self.var2.set('')
	
	# back()
	def back(self):
	        self.TEXT = self.TEXT[:-1]
	        self.var.set(self.TEXT)
	
	
	# square ()
	
	def square(self):
	        try:
	            self.TEXT = int(self.TEXT) ** 2
	            self.var.set(self.TEXT)
	            self.var2.set(f"{self.TEXT}\u00B2")
	            self.TEXT = str(self.TEXT)
	        except:
	            self.var.set('Error')
	         
	        
	        
	        
	        
	        
	
if __name__ == "__main__":
	C = Calculator()
	C.run()