class Solution:
    def unique_paths(self, obstacle_grid: [[int]]) -> int:
        m = len(obstacle_grid)  # 网格的行数
        n = len(obstacle_grid[0])  # 网格的列数
        dp = [[0] * n for _ in range(m)]
        if obstacle_grid[m - 1][n - 1] == 1 or obstacle_grid[0][0] == 1:
            # 如果起点或终点有障碍物，直接返回0
            return 0
        if obstacle_grid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        for i in range(m):
            if obstacle_grid[i][0] == 0:
                dp[i][0] = 1
        for j in range(n):
            if obstacle_grid[0][j] == 0:
                dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacle_grid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    solution = Solution()
    print(solution.unique_paths(obstacle_grid))
