
'''
https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?
tpId=13&tqId=23269&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''



class Solution:
    def minNumberInRotateArray(self, nums: list[int]) -> int:
        first = nums[0]
        for i in range(len(nums)):
            if nums[i] < first:
                return nums[i]
        return first


if __name__ == '__main__':
    nums = [3, 100, 200, 3]
    val = Solution().minNumberInRotateArray(nums)
    print(val)
