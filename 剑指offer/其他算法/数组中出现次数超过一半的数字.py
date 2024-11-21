'''
https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?
tpId=13&tqId=23271&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers: list[int]) -> int:
        length = len(numbers)
        hashMap = dict()
        for num in numbers:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
            if hashMap[num] > length / 2:
                return num
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    val = Solution().MoreThanHalfNum_Solution(nums)
    print(val)
