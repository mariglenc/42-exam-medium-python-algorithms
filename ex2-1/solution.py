def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return lists

    common = set(lists[0])

    for lst in lists[1:]:
        common &= set(lst)

    return sorted(common)
