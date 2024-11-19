'''
https://www.nowcoder.com/practice/57d85990ba5b440ab888fc72b0751bf8?tpId=13
&tqId=587690&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking&sourceUrl=
%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
递归法解题。每次都分别取i和长度n-i绳子最大值相乘获得最大值
'''

class Solution:
    def __init__(self):
        # 关键代码，设定一个初始值，比如4分成2+2两段。那么2的乘积最大值应该为2而不是1
        self.dic = {1: 1, 2: 2, 3: 3}

    def cutRope(self, n: int) -> int:
        # 因为至少要分成两段，所以这里和self.dic的初始值不同
        if n < 4:
            return n - 1
        return self.maxCutLength(n)

    def maxCutLength(self, n: int) -> int:
        if n in self.dic:  # 关键代码：如果该n下的乘积最大值计算过且记录过直接返回答案，减少计算量
            return self.dic[n]
        maxLength = 1
        for i in range(1, n):
            cutLength = self.maxCutLength(n - i)
            maxLength = max(maxLength, cutLength * i)
        self.dic[n] = maxLength
        return maxLength


if __name__ == '__main__':
    val = Solution().cutRope(9)
    print(val)
