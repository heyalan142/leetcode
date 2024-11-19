class Solution:
    # 递归法：dp[i]表示前i个数的译码方法有多少种。
    def solve(self, nums: str) -> int:
        if nums == "0":
            return 0
        if nums == "10" or nums == "20":
            return 1
        # 关键代码：当0的前面不是1或2时，无法译码，0种
        for i in range(1, len(nums)):
            if nums[i] == '0':
                if nums[i - 1] != '1' and nums[i - 1] != '2':
                    return 0
        dp = [1 for _ in range(len(nums) + 1)]
        for i in range(2, len(nums) + 1):
            subNums = nums[(i - 2):i]
            subNum = int(subNums)
            if 11 <= subNum <= 26 and subNum != 20:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[len(nums)]


if __name__ == '__main__':
    string = "7256224241262422162912798142114"
    val = Solution().solve(string)
    print(val)
