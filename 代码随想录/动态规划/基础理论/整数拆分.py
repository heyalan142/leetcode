class Solution:
    def integer_break(self, n: int) -> int:
        dp = [0] * (n + 1)  # 创
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)
        return dp[n]


if __name__ == '__main__':
    n = 10
    solution = Solution()
    print(solution.integer_break(n))
