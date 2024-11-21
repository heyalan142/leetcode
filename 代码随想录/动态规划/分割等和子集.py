def can_partition(nums: [int]) -> bool:
    sum = 0
    for num in nums:
        sum += num
    if sum % 2 != 0:
        return False
    target = sum // 2
    dp = [0] * (target + 1)
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = max(dp[j], dp[j-num] + num)
    if dp[target] == target:
        return True
    return False


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    sum = 0
    for num in range(len(nums)):
        sum += num
    print(can_partition(nums))
