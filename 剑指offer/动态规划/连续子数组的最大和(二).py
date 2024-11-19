

class Solution:

    # 递归法：dp[i]为求得最大和子数组最后一位一定是array[i]的数组的最大值
    def FindGreatestSumOfSubArray(self, array: list[int]) -> list[int]:
        # write code here
        dp = [0 for _ in range(len(array))]
        dp[0] = array[0]
        left = 0
        right = 0
        maxSum = dp[0]
        maxLeft = 0
        maxRight = 0
        for i in range(1, len(array)):
            right += 1
            # 关键代码，dp[i - 1] + array[i] 要大于等于，包括等于 array[i]。因为等于的时候dp[i - 1] + array[i]长度最长
            if dp[i - 1] + array[i] >= array[i]:
                dp[i] = dp[i - 1] + array[i]
            else:
                dp[i] = array[i]
                left = right
            if maxSum < dp[i] or (maxSum == dp[i] and right -left > maxRight - maxLeft):
                maxSum = dp[i]
                maxLeft = left
                maxRight = right
        return array[maxLeft:maxRight + 1]


if __name__ == '__main__':
    nums = [1, 2, -3, 4, -1, 1, -3, 2]
    val = Solution().FindGreatestSumOfSubArray(nums)
    print(val)
