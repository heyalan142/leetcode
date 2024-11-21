def move_zeroes(nums: [int]) -> list[int]:
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            temp = nums[slow]
            nums[slow] = nums[fast]
            nums[fast] = temp
            slow += 1
        fast += 1
    return nums


if __name__ == '__main__':
    nums = [1, 2, 0, 1, 0, 3, 12]
    print(move_zeroes(nums))
