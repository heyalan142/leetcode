class Solution:
    def fiber(self, cost:[int]) -> int:
        if len(cost) == 0:
            return 0
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            cost1 = cost[i - 1]
            cost2 = cost[i - 2]
            dp[i] = min(dp[i - 1] + cost1, dp[i - 2] + cost2)
        return dp[len(cost)]


if __name__ == '__main__':
    cost = [10, 15, 20]
    solution = Solution()
    print(solution.fiber(cost))
