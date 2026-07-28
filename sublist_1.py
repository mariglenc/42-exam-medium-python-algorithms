def sublist(lst: list[int], k: int) -> list[int]:
	length = len(lst)
	result = []

	for i in range(length):
		if length - i < k:
			break
		result.append(max(lst[i: i+k]))
	
	return result

print(sublist([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))

print(sublist([1, 2, 3, 4, 5], 2))  # Output: [2, 3, 4, 5]
print(sublist([5, 4, 3, 2, 1], 3))  # Output: [5, 4, 3]
print(sublist([1, 3, 2, 5, 4], 1))  # Output: [1, 3, 2, 5, 4]

