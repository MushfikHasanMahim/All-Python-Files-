# code for implementing Stack DataStracture

my_list = [3, 8, 1, 6, 4, 2]


def implement_stack(my_list):
	for i in range(len(my_list)):
		for j in range(len(my_list)-1):
			if my_list[j] > my_list[j+1]:
				my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
	
	
	print(my_list)
	
	
implement_stack(my_list)