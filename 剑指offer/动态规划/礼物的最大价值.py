class Solution:
    # 递归法：dp[i][j]走到(i,j)点时礼物的最大价值
    def maxValue(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for j in range(1, row):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = max(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
        return dp[row - 1][col - 1]


if __name__ == '__main__':
    data = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = Solution().maxValue(data)
    num = 7
    val = Solution().jumpFloor(num)
    print(val)
