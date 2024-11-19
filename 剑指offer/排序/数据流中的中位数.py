class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        if len(self.nums) <= 0:
            self.nums.append(num)
        else:
            index = 0
            while index < len(self.nums):
                if num <= self.nums[index]:
                    break
                index = index + 1
            self.nums.insert(index, num)

    def GetMedian(self):
        length = len(self.nums)
        if length <= 0:
            return 0
        if length % 2 == 0:
            mid = length // 2
            return (self.nums[mid] + self.nums[mid - 1]) / 2
        else:
            mid = length // 2
            return self.nums[mid]


if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    result = Solution().GetMedian()
    print(result)
