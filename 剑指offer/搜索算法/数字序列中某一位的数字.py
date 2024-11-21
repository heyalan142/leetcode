'''
https://www.nowcoder.com/practice/29311ff7404d44e0b07077f4201418f5?
tpId=13&tqId=2285751&ru=/exam/oj/ta&qru=/ta/coding-interviews/
question-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        sum = 9
        start = 1
        while n > sum:
            n -= sum
            start *= 10
            digit += 1
            sum = 9 * digit * start
        num = start + (n - 1) // digit
        index = (n - 1) % digit
        return int(str(num)[index])


if __name__ == '__main__':
    n = 15
    val = Solution().findNthDigit(n)
    print(val)
