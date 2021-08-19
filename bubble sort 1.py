# Bubble_sort algorithm for sorting letters


def sort_letters(s):
	for i in range(len(s)-1):
		for j in range(len(s)-1):
			if ord(s[j]) > ord(s[j + 1]):
				s[j], s[j+1] = s[j+1], s[j]
	return s
	
print(sort_letters(['a', 'A', 'd', 'c']))