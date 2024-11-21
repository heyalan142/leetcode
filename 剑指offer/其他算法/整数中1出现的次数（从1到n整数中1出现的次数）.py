# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/bd7f978302044eee894445e244c7eee6?
tpId=13&tqId=23272&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

具体做法：
step 1：从1遍历到n，查看每一个数字。
step 2：对于每个数字，用连除法每次判断最后一位数字是否为1，并进行计数。
'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        result = 0
        for i in range(1, n + 1):
            j = i
            while j > 0:
                if j % 10 == 1:
                    result += 1
                j = j // 10
        return result


if __name__ == '__main__':
    n = 13
    val = Solution().NumberOf1Between1AndN_Solution(n)
    print(val)

# write code here
