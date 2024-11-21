def max_length_of_sublist(nums: [int]) -> int:
    if len(nums) <= 0:
        return 0
    dp = [1] * len(nums)
    result = 1
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            dp[i + 1] = dp[i] + 1
        result = max(result, dp[i + 1])
    return result


if __name__ == '__main__':
    nums = nums = [1, 3, 5, 4, 7]
    print(max_length_of_sublist(nums))
