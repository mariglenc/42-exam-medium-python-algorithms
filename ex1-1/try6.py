# ex1-1 - sort_list_of_lists
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
    sorted_list = []

    for ls in lst:
        sorted_list.append(sorted(ls))
    
    return sorted_list
