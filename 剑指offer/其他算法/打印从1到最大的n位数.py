'''
https://www.nowcoder.com/practice/4436c93e568c48f6b28ff436173b997f?tpId=13&tqId=
2273153&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking&sourceUrl=%2Fexam
%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def printNumbers(self, n: int) -> list[int]:
        num = 1
        while n > 0:
            num = num * 10
            n -= 1

        results = []
        for i in range(1, num):
            results.append(i)
        return results


if __name__ == '__main__':
    val = Solution().printNumbers(3)
    print(val)
