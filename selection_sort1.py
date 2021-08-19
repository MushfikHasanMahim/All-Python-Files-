# Selection Sort Algorithem


def selection_sort(array):
	sorted_array = []
	for i in range(len(array)):
		minimum = min(array)
		sorted_array.append(minimum)
		array.remove(minimum)
	return sorted_array


print(selection_sort([5, 7, 2, 9, 1, 4]))
		