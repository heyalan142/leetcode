class Solution:
    def backtracking(self, n: int, k: int, start_index: int, path: [int], result: [list[int]]) -> None:
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start_index, n + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()

    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 3))
