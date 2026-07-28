def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
    return [sorted(x) for x in lst]
