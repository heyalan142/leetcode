
'''
https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?
tpId=13&tqId=23261&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


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
