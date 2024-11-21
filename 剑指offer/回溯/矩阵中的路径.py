'''
https://www.nowcoder.com/practice/2a49359695a544b8939c77358d29b7e6?
tpId=13&tqId=1517966&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:

    def hasPath(self, matrix: list[list[str]], word: str) -> bool:
        if len(word) <= 0:
            return False
        maxRow = len(matrix)
        if maxRow <= 0:
            return False
        maxCol = len(matrix[0])
        if maxCol <= 0:
            return False
        flag = [[False for _ in range(maxCol)] for _ in range(maxRow)]
        for i in range(maxRow):
            for j in range(maxCol):
                if self.dfs(matrix, i, j, 0, word, flag):
                    return True
        return False

    def dfs(self, matrix: list[list[str]], row: int, col: int, k: int, word: str, flag: list[list[bool]]):
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        if row < 0 or row > maxRow - 1 or col < 0 or col > maxCol - 1 or flag[row][col] or matrix[row][col] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        flag[row][col] = True
        isEqualRowNextStr = self.dfs(matrix, row + 1, col, k + 1, word, flag)
        isEqualColNextStr = self.dfs(matrix, row, col + 1, k + 1, word, flag)
        isEqualRowFrontStr = self.dfs(matrix, row - 1, col, k + 1, word, flag)
        isEqualColFrontStr = self.dfs(matrix, row, col - 1, k + 1, word, flag)
        if isEqualRowNextStr or isEqualColNextStr or isEqualRowFrontStr or isEqualColFrontStr:
            return True
        flag[row][col] = False
        return False


if __name__ == '__main__':
    matrix = [["A", "A", "A", "A"], ["A", "A", "A", "A"], ["A", "A", "A", "A"]]
    word = "AAAAAAAAAAAA"
    val = Solution().hasPath(matrix, word)
    print(val)
