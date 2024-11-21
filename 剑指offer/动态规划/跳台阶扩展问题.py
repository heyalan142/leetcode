'''
https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?
tpId=13&tqId=23262&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
对于最后一级台阶，我们可以由倒数第二级台阶跳1步，也可以由倒数第三级跳两步，即
f(n)=f(n−1)+f(n−2)+...+f(n−(n−1))+f(n−n)=f(0)+f(1)+f(2)+...+f(n−1)，因为
f(n−1)=f(n−2)+f(n−3)+...+f((n−1)−(n−2))+f((n−1)−(n−1))，经整理得
f(n)=f(n−1)+f(n−1)=2∗f(n−1)，因此每级台阶方案数是前面一级台阶方案数的2倍。
'''


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
