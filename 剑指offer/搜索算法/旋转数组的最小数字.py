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
