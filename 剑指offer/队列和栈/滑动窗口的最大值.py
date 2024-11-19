from collections import deque

'''
# 用队列实现。p
push操作，把队列里大于value的值从右侧弹出再将value加入队列
pop操作，队列最前面的元素是value，左侧弹出，否则不处理
maxInWindows，每次pop再push,得到结果保存出来
'''
class MaxWindowQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution:
    def maxInWindows(self, nums: list[int], size: int) -> list[int]:
        result = []
        if size == 0 or size > len(nums):
            return result
        maxWindowQueue = MaxWindowQueue()
        for i in range(size):
            maxWindowQueue.push(nums[i])
        result.append(maxWindowQueue.front())
        for i in range(size, len(nums)):
            maxWindowQueue.pop(nums[i - size])
            maxWindowQueue.push(nums[i])
            result.append(maxWindowQueue.front())
        return result


if __name__ == '__main__':
    nums = [10, 14, 12, 11], 0
    size = 0
    maxValue = Solution().maxInWindows(nums, size)
    print(maxValue)

