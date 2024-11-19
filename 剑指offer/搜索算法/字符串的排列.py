import str as str


class Solution:
    def backtracking(self, letters: [str], used: [bool], path: [str], result: [list[str]]) -> None:
        if len(path) == len(letters):
            result.append("".join(path[:]))
            return
        for i in range(len(letters)):
            if (i > 0 and letters[i] == letters[i - 1] and not used[i - 1]) or used[i]:
                continue
            used[i] = True
            path.append(letters[i])
            self.backtracking(letters, used, path, result)
            path.pop()
            used[i] = False

    def Permutation(self, str: str) -> list[str]:
        letters = list(str)
        letters.sort()
        result = []
        path = []
        used = [False] * len(letters)
        self.backtracking(letters, used, path, result)
        return result

if __name__ == '__main__':
    str = "aba"
    val = Solution().Permutation(str)
    print(val)
