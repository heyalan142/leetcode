def min_sublist_lenth(nums: list[int], target: int) -> int:
    left = 0
    sum_value = 0
    min_length = len(nums)
    right = 0
    while right < len(nums):
        sum_value += nums[right]
        while sum_value >= target:
            sum_value = sum_value - nums[left]
            min_length = min(min_length, right - left + 1)
            left += 1
        right += 1
    return min_length


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    value = 7
    result = min_sublist_lenth(nums, value)
    print(result)
