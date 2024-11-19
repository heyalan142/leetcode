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
