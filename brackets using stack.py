print('I am gonna be a pythonista :)')


def need_brackets(brackets):
	starting_brackets = []
	for i in brackets:
		if i in ['(', '{', '[']:
			starting_brackets.append(i)
		else:
		  current_bracket = starting_brackets.pop()
		  if current_bracket == '[':
		  	if i != ']':
		  		return False
		  elif current_bracket == '{':
		  	if i != '}':
		  		return False
		  
		  else:
		  	if i != ')':
		  		return False
	if starting_brackets:
	   return False
	else:
	   return True
	   

	
while True:
    inputs = input('Enter brackets -->')
    if inputs == 'q':
    	break
    else:
    	if need_brackets(inputs):
    		print('Correct ✓')
    	else:
    		print('Wrong x')



   