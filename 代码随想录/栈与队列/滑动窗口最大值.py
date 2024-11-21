from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value: int):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value: int):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


def max_sliding_window(nums: [int], k: int) -> list:
    result = []
    my_queue = MyQueue()
    for i in range(k):
        my_queue.push(nums[i])
    result.append(my_queue.front())
    for i in range(k, len(nums)):
        my_queue.pop(nums[i - k])
        my_queue.push(nums[i])
        result.append(my_queue.front())  # 记录对应的最大值
    return result


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window(nums, 3))
