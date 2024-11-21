def valid_mountain_array(nums: [int]) -> bool:
    if len(nums) < 3:
        return False
    left = 0
    right = len(nums) - 1
    while nums[left] < nums[left + 1] and left < len(nums) - 1:
        left += 1
    while nums[right] < nums[right - 1] and right > 0:
        right -= 1
    return left == right


if __name__ == '__main__':
    nums = [0, 3, 2, 1]
    target = 2
    result = valid_mountain_array(nums)
    print(result)
