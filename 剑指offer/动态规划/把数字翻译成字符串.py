'''
https://www.nowcoder.com/practice/48d2ff79b8564c40a50fa79f9d5fa9c7?
tpId=13&tqId=2276769&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
对于普通数组1-9，译码方式只有一种，但是对于11-19，21-26，译码方式有可选择的两种方案，因
此我们使用动态规划将两种方案累计。

具体做法：
step 1：用辅助数组dp表示前i个数的译码方法有多少种。
step 2：对于一个数，我们可以直接译码它，也可以将其与前面的1或者2组合起来译码：如果直接译码，则
dp[i]=dp[i−1]；如果组合译码，则dp[i]=dp[i−2]。
step 3：对于只有一种译码方式的，选上种dp[i−1]即可，对于满足两种译码方式（10，20不能）则是dp[i−1]+dp[i−2]
step 4：依次相加，最后的dp[length]即为所求答案。
'''


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
