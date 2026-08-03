# ex1-1 - sort_list_of_lists
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
    sorted_list=[] # declare an empty list
    for ls in lst: # iterate over all lst items
        sorted_list.append(sorted(ls)) # sort them and append to the sorted lst
    
    return sorted_list # return it