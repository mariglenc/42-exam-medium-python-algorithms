#def merge_sort_unique(list):
#	result = set()

#	for lst in list:
#		result.update(lst)
	
#	return sorted(result)




#def merge_sort_unique(lists):
#    return sorted(set(num for lst in lists for num in lst))

def merge_sort_unique(lists):
    return sorted(set(x for y in lists for x in y))

    return sorted(set(x for y in lists for x in y))

    return sorted(set(x for y in lists for x in y))

    return sorted(set(x for y in lists for x in y))

    return sorted(set(x for y in lists for x in y))

    return sorted(set(x for y in lists for x in y))
lists = [[1, 3, 5], [2, 3, 6], [1, 7]]
print(merge_sort_unique(lists))