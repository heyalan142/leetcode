class Solution:
    def backtracking(self, nums: list[int], target_sum: int, current_sum: int, start_index: int, path: [int],
                     result: [list[int]]) -> None:
        if current_sum > target_sum:
            return
        if current_sum == target_sum:
            result.append(path[:])
            return
        for i in range(start_index, len(nums)):
            current_sum += nums[i]
            path.append(nums[i])
            self.backtracking(nums, target_sum, current_sum, i, path, result)
            current_sum -= nums[i]
            path.pop()

    def combine(self, nums: list[int], target_sum: int) -> list[list[int]]:
        result = []
        start_index = 0
        total_sum = 0
        self.backtracking(nums, target_sum, total_sum, start_index, [], result)
        return result


if __name__ == '__main__':
    nums = [2, 3, 5]
    solution = Solution()
    print(solution.combine(nums, 8))
