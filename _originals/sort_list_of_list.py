def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
	# return [sorted(x) for x in lst]
	return [sorted(x) for x in lst]


print(sort_list_of_lists([[3, 1, 2], [6, 5, 4], [9, 8, 7]]))
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sort_list_of_lists([[10, 9], [8, 7], [6, 5]]))
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sort_list_of_lists([[10, 9], [8, 7], [6, 5]]))
# Output: [[9, 10], [7, 8], [5, 6]]
print(sort_list_of_lists([[1], [3, 2], [5, 4, 6]]))
# Output: [[1], [2, 3], [4, 5, 6]]

