def find_target_sum_ways(nums: [int]) -> int:
    sum = 0
    for num in nums:
        sum += num
    target = sum // 2
    dp = [0] * (target + 1)
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = max(dp[j], dp[j - num] + num)
    return sum - dp[target] - dp[target]


if __name__ == "__main__":
    nums = [2, 7, 4, 1, 8, 1]
    sum = 0
    for num in range(len(nums)):
        sum += num
    print(find_target_sum_ways(nums))
