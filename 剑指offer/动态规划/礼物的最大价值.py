'''
https://www.nowcoder.com/practice/2237b401eb9347d282310fc1c3adb134?
tpId=13&tqId=2276652&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
如果我们现在已经身处最右下角的一个格子，获取了这个礼物，那我们肯定是加上来自
左边累计的最大礼物价值与来自上边累计的最大礼物价值的较大值，这样我们能获取的
礼物价值才会更大，因此我们用dp[i][j]表示从左上角到第i行第j列的格子总共能获取的最大价值，因此转移方程为
dp[i][j]=grid[i][j]+max(dp[i−1][j],dp[i][j−1]).

具体做法：
step 1：初始化第一列，每个元素只能累加自上方。
step 2：初始化第一行，每个元素只能累加自左方。
step 3：然后遍历数组，对于每个元素添加来自上方或者左方的较大值。
'''


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
                dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])
        return dp[row - 1][col - 1]


if __name__ == '__main__':
    data = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = Solution().maxValue(data)
    print(result)
