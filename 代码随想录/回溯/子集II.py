class Solution:

    def backtracking(self, nums: list[int], startIndex: int, used, path: [int], result: [list[int]]) -> None:
        result.append(path[:])  # 收集子集
        for i in range(startIndex, len(nums)):
            # used[i - 1] == True，说明同一树枝 nums[i - 1] 使用过
            # used[i - 1] == False，说明同一树层 nums[i - 1] 使用过
            # 而我们要对同一树层使用过的元素进行跳过
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, i + 1, used, path, result)
            used[i] = False
            path.pop()

    def combine(self, nums: list[int]) -> list[list[int]]:
        result = []
        start_index = 0
        path = []
        used = [False] * len(nums)
        nums.sort() 
        self.backtracking(nums, start_index, used, path, result)
        return result


if __name__ == '__main__':
    nums = [1, 2, 2]
    solution = Solution()
    print(solution.combine(nums))
