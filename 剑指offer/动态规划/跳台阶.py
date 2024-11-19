class Solution:
    # 递归法：dp[i]为跳上n级的台阶总共有多少种跳法
    def jumpFloor(self, number: int) -> int:
        if number < 2:
            return 1
        # write code here
        dp = [0 for _ in range(number + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]


if __name__ == '__main__':
    num = 7
    val = Solution().jumpFloor(num)
    print(val)
