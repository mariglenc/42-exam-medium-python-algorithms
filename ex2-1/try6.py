# ex2-1 - list_intersection
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    unique_nums = set(lists[0])
    for ls in lists[1:]:
        unique_nums = unique_nums & set(ls)
    
    return sorted(unique_nums)
