'''
https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?
tpId=13&tqId=23445&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

B[0]    [ 1,   A[1], A[2],.......,A[n-2], A[n-1]]
B[1]    [A[0],  1,   A[2],.......,A[n-2], A[n-1]]
B[2]    [A[0], A[1],   1,.........A[n-2], A[n-1]]
.....
B[n-2]  [A[0], A[1], A[2],.......,.. 1,    A[n-1]]
B[n-1]  [A[0], A[1], A[2],.......,A[n-2],    1  ]

具体做法：
step 1：初始化数组B，第一个元素为1.
step 2：从左到右遍历数组A，将数组B的前一个数与数组A的前一个数相乘就得到了下三角中数组B的当前数。
step 3：再从右到左遍历数组A，用一个数字记录从右到左上三角中的累乘，每次只会乘上一个数，同时给数组B对应部分也乘上该累乘。
'''


class Solution:
    def multiply(self, A: list[int]) -> list[int]:
        B = [1 for _ in range(len(A))]
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        # 关键代码：再乘右边，从右到左
        for i in reversed(range(len(A))):
            B[i] *= temp
            temp *= A[i]
        return B


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    val = Solution().multiply(A)
    print(val)
