class Solution:
    def backtracking(self, nums: list[int], used:[],  path: [int], result: [list[int]]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(0, len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, used, path, result)
            path.pop()
            used[i] = False

    def combine(self, nums: list[int]) -> list[list[int]]:
        result = []
        used = [False] * len(nums)
        self.backtracking(nums, used, [], result)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.combine(nums))
