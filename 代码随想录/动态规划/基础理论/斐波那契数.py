class Solution:
    def fiber(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.fiber(n))
