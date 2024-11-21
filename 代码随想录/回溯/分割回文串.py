class Solution:

    def is_palindrome(self, string: str) -> bool:
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    def backtracking(self, string: str, start_index: int, path: [int], result: [list[int]]) -> None:
        if start_index == len(string):
            result.append(path[:])
            return
        for i in range(start_index, len(string)):
            sub_string = string[start_index:i + 1]
            if self.is_palindrome(sub_string):
                path.append(sub_string)
                self.backtracking(string, i + 1, path, result)
                path.pop()

    def combine(self, string: str) -> list[str]:
        result = []
        start_index = 0
        self.backtracking(string, start_index, [], result)
        return result


if __name__ == '__main__':
    string = "aab"
    solution = Solution()
    print(solution.combine(string))
