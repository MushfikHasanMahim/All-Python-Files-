# let's implement stack


def neat_brackets(input):
    stack = []
    for letter in input:
        if letter in '[({':
            stack.append(letter)
        else:
            current_bracket = stack.pop()
            if current_bracket == '(':
                if letter != ')':
                    return False
            if current_bracket == '{':
                if letter != '}':
                    return False
            if current_bracket == ']':
                if letter != ']':
                    return False 
                    
    if stack:
        return False
    return True
    
    
print(neat_brackets(input('Enter : ')))
                 
             