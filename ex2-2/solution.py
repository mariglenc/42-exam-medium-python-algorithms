def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
