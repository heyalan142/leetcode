def search_insert_index(nums: [int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if target > nums[middle]:
            left = middle + 1
        elif target < nums[middle]:
            right = middle - 1
        else:
            return middle
    return right + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    result = search_insert_index(nums, target)
    print(result)
