#def sliding_w_m(ar, shift):
#	k = shift
#	n = len(ar)
#	i = 0
#	res = []
#	while (i < n):
#		if (n - i < k):
#			break
#		j = i
#		temp = []
#		while (j < i + k):
#			temp.append(ar[j])
#			j += 1
#		i += 1
#		res.append(max(temp))
#	return res

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]


    if not nums or k <= 0 or k > len(nums):
        return []
    
    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]


print(sliding_w_m([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
print(sliding_w_m([1], 3))
print(sliding_w_m([1, 2, 3], 2))
print(sliding_w_m([1, 2], 8))
print(sliding_w_m([], 3))
