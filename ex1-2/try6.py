# ex1-2 - merge_sort_unique
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    merged_list = []
    for ls in lists:
        for item in ls:
            merged_list.append(item)
    
    unique = set(merged_list)
    
    return sorted(unique)
