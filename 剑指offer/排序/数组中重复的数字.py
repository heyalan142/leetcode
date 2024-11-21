'''
https://www.nowcoder.com/practice/6fe361ede7e54db1b84adc81d09d8524?
tpId=13&tqId=1375279&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def duplicate(self, numbers: list[int]) -> int:
        hashMap = dict()
        for num in numbers:
            if num in hashMap:
                return num
            else:
                hashMap[num] = 1
        return -1


if __name__ == '__main__':
    data = [2, 3, 1, 0, 2, 5, 3]
    result = Solution().duplicate(data)
    print(result)
