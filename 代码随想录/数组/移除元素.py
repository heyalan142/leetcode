def remove_element(nums: list[int], value: int) -> int:
    slow = 0
    fast = 0
    size = len(nums) - 1
    while fast <= size:
        if nums[fast] != value:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    value = 2
    result = remove_element(nums, value)
    print(result)
