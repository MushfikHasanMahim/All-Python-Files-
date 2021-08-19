def fizz_buzz(i):
	if i % 3 == 0 and i % 5 == 0:
		return 'FizzBuzz'
	elif i % 3 == 0:
		return 'Fizz'
	elif i % 5 == 0:
		return 'Buzz'
	return i
		
		
while True:
	i = int(input())
	if i != 0:
		print(fizz_buzz(i))
	else:
		break