'''
https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?
tpId=13&tqId=23291&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
思路：用回溯法排列出来，不用startIndex,但是用used表示是否使用过，因为有重复的，要
加判断letters[i] == letters[i - 1] and not used[i - 1]
'''

import str as str


class Solution:
    def backtracking(self, letters: [str], used: [bool], path: [str], result: [list[str]]) -> None:
        if len(path) == len(letters):
            result.append("".join(path[:]))
            return
        for i in range(len(letters)):
            # 关键代码
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
