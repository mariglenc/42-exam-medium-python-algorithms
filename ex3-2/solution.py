def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False

    if not arr1 and not arr2:
        return True

    return any(
        arr2 == arr1[i:] + arr1[:i]
        for i in range(len(arr1))
    )
