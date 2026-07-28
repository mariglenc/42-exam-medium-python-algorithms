def sliding_w_m(ar, k):
    length = len(ar)
    result = []
    i = 0

    while i < length:
        if length - i < k:
            break
        j = i
        temp = []
        while j < i + k:
            temp.append(ar[j])
            j += 1
        i += 1
        result.append(max(temp))
    return result 


print(sliding_w_m([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))

# print(sliding_w_m([1], 3))

# print(sliding_w_m([1, 2, 3], 2))

# print(sliding_w_m([1, 2], 1))
	
# print(sliding_w_m([1, 5, 1, 5, 1, 5, 2], 3))  # Output: [2, 3, 4, 5]
# print(sliding_w_m([5, 4, 3, 2, 1], 3))  # Output: [5, 4, 3]
# print(sliding_w_m([1, 3, 2, 5, 4], 1))  # Output: [1, 3, 2, 5, 4]