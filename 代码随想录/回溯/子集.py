class Solution:
    def backtracking(self, nums: list[int], start_index: int, path: [int], result: [list[int]]) -> None:
        result.append(path[:])
        if start_index >= len(nums):
            return
        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()

    def combine(self, nums: list[int]) -> list[list[int]]:
        result = []
        start_index = 0
        self.backtracking(nums, start_index, [], result)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.combine(nums))
