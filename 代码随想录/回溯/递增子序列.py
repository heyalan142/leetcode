class Solution:
    def backtracking(self, nums: list[int], start_index: int, path: [int], result: [list[int]]) -> None:
        if len(path) > 1:
            result.append(path[:])
        if start_index >= len(nums):
            return
        uset = set()  # 使用集合对本层元素进行去重
        for i in range(start_index, len(nums)):
            if (len(path) > 0 and nums[i] < path[-1]) or nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()

    def combine(self, nums: list[int]) -> list[list[int]]:
        result = []
        start_index = 0
        self.backtracking(nums, start_index, [], result)
        return result


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    solution = Solution()
    print(solution.combine(nums))
