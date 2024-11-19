

class Solution:
    # 递归法：dp[i]为跳上n级的台阶总共有多少种跳法
    def Fibonacci(self, n: int) -> int:
        if n < 2:
            return 1
        # write code here
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]



if __name__ == '__main__':
    num = 4
    val = Solution().Fibonacci(num)
    print(val)
