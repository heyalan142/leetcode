def half_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2  # 定义target在左闭右闭的区间里，[left, right]
        if nums[middle] < target:
            left = middle + 1  # target在右区间，所以[middle + 1, right]
        elif nums[middle] > target:
            right = middle - 1  # target在左区间，所以[left, middle - 1]
        else:
            return middle  # 数组中找到目标值，直接返回下标
    return -1  # 未找到目标值


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 12
    result = half_search(nums, target)
    print(result)
