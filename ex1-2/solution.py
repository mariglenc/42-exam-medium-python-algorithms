def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    return sorted(set(x for y in lists for x in y))
