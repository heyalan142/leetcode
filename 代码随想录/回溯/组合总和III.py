class Solution:
    def backtracking(self, nums: [int], k: int, target_sum: int, current_sum: int, start_index: int, path: [int],
                     result: [list[int]]) -> None:
        if current_sum > target_sum:
            return
        if len(path) == k:
            if current_sum == target_sum:
                result.append(path[:])
            return
        for i in range(start_index, len(nums)):
            current_sum += nums[i]
            path.append(nums[i])
            self.backtracking(nums, k, target_sum, current_sum, i + 1, path, result)
            current_sum -= nums[i]
            path.pop()

    def combine(self, nums: [int], k: int, target_sum: int) -> list[list[int]]:
        result = []
        start_index = 0
        total_sum = 0
        self.backtracking(nums, k, target_sum, total_sum, start_index, [], result)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solution = Solution()
    print(solution.combine(nums, 3, 9))
