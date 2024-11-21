
'''
https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?
tpId=13&tqId=23263&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''



class Solution:
    def GetLeastNumbers_Solution(self, input: list[int], k: int) -> list[int]:
        if k == 0 or len(input) == 0:
            return []
        else:
            input.sort()
            return input[:k]


if __name__ == '__main__':
    input = [4, 5, 1, 6, 2, 7, 3, 8]
    k = 4
    result = Solution().GetLeastNumbers_Solution(input, 4)
    print(result)
