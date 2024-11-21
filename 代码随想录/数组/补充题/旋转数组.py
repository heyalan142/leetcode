def rotate(nums: [int], k: int) -> list[int]:
    for i in range(k):
        temp = nums[-1]
        for j in range(len(nums) - 1, 0, -1):
            nums[j] = nums[j - 1]
        nums[0] = temp
    return nums


if __name__ == '__main__':
    nums = [-1, -100, 3, 99]
    print(rotate(nums, 2))
