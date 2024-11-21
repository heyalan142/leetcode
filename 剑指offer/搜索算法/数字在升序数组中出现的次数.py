
'''
https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?
tpId=13&tqId=23274&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def GetNumberOfK(self, nums: list[int], k: int) -> int:
        count = 0
        for num in nums:
            if num == k:
                count += 1
        return count


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    k = 3
    val = Solution().GetNumberOfK(nums, k)
    print(val)
