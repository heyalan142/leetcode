'''
https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?
tpId=13&tqId=23255&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
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
