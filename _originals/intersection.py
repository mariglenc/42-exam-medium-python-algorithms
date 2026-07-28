# return the numbers that appear in all lists, 
# sorted in a new list, removing duplicates


def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return lists

    common = set(lists[0])

    for lst in lists[1:]:
        common &= set(lst)

    return sorted(common)


    if not lists:
        return lists
    
    common = set(lists[0])

    for lst in lists[1:]:
        common &= set(lst)
    
    return sorted(common)


    if not lists:
        return lists
    
    common = set(list[0])

    for lst in lists[1:]:
        common &= set(lst)
    
    return sorted(common)


    if not lists:
        return lists
    
    common = set(lists(0))

    for lst in lists[1:]:
        common &= set(lst)
    
    return sorted(common)


    if not lists:
        return lists
    
    common = set(lists(0))

    for lst in list[1:]:
        common &= set(lst)
    
    return sorted(common)

    if not lists:
        return lists
    
    common = set(lists(0))

    for lst in lists[1:]:
        common &= set(lst)

    return sorted(common)


    if not lists:
        return lists
    
    common = set(lists(0))

    for lst in list[1:]:
        common &= set(lst)
    return sorted(common)


    if not lists:
        return lists
    
    common = set(lists(0))

    for lst in lists[1:]:
        common &= set(lst)
    return sorted(common)

print(list_intersection([[5, 4, 3], [2, 1, 3], [2, 1, 3]]))
print(list_intersection([[5, 4, 3], [2, 1, 6], [7, 0, 9]]))
