

class Solution:
    # 递归法：dp[i]为跳上n级的台阶总共有多少种跳法
    def jumpFloorII(self, number: int) -> int:
        if number < 2:
            return 1
        # write code here
        dp = [0 for _ in range(number + 1)]
        dp[1] = 1
        for i in range(2, number + 1):
            dp[i] = 2 * dp[i - 1]
        return dp[number]



if __name__ == '__main__':
    num = 3
    val = Solution().jumpFloorII(num)
    print(val)
