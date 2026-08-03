# ex1-1 - sort_list_of_lists
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
    sorted_list = []
    for inner_lst in lst:
        sorted_list.append(sorted(inner_lst))
    return sorted_list

