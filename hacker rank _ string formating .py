def print_formatted(number):
    L = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        
        print(f'{" " * (L -len(str(i))) + str(i)}',
         f'{" " * (L -len(str(oct(i))[2:])) + str(oct(i))[2:]}',
         f'{" " * (L -len(str(hex(i))[2:])) + str(hex(i))[2:].upper()}',
         f'{" " * ((len(str(bin(number)[2:]))) - (len(str(bin(i))[2:])) ) + str(bin(i))[2:]}')
        
  
number = 63     
print_formatted(number)   

