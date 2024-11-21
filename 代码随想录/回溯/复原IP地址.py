class Solution:
    def is_valid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:  # 0开头的数字不合法
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():  # 遇到非数字字符不合法
                return False
            num = num * 10 + int(s[i])
            if num > 255:  # 如果大于255了不合法
                return False
        return True

    def backtracking(self, string: str, start_index: int, path: [int], result: [list[int]]) -> None:
        if len(path) > 4:  # 剪枝
            return
        if start_index == len(string) and len(path) == 4:
            result.append('.'.join(path))
            return
        for i in range(start_index, len(string)):
            if self.is_valid(string, start_index, i):
                sub_string = string[start_index:i + 1]
                path.append(sub_string)
                self.backtracking(string, i + 1, path, result)
                path.pop()

    def combine(self, string: str) -> list[str]:
        result = []
        start_index = 0
        self.backtracking(string, start_index, [], result)
        return result


if __name__ == '__main__':
    string = "010010"
    solution = Solution()
    print(solution.combine(string))
