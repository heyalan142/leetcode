'''
https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?
tpId=13&tqId=23460&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def __init__(self):
        self.res = 0

    def calSum(self, number: int) -> int:
        sum = 0
        while number:
            sum += (number % 10)
            number //= 10
        return sum

    def movingCount(self, threshold: int, rows: int, cols: int) -> int:
        if threshold <= 0:
            return 1
        if rows <= 0:
            return 1
        if cols <= 0:
            return 1
        flag = [[False for _ in range(cols)] for _ in range(rows)]
        self.dfs(threshold, rows, cols, 0, 0, flag)
        return self.res

    def dfs(self, threshold: int, rows: int, cols: int, row: int, col: int, flag: list[list[bool]]):
        if row < 0 or col < 0 or row > rows - 1 or col > cols - 1 or flag[row][col]:
            return
        calTotal = self.calSum(row) + self.calSum(col)
        if calTotal > threshold:
            return
        flag[row][col] = True
        self.res += 1
        self.dfs(threshold, rows, cols, row + 1, col, flag)
        self.dfs(threshold, rows, cols, row - 1, col, flag)
        self.dfs(threshold, rows, cols, row, col + 1, flag)
        self.dfs(threshold, rows, cols, row, col - 1, flag)


if __name__ == '__main__':
    threshold = 15
    rows = 100
    cols = 100
    val = Solution().movingCount(threshold, rows, cols)
    print(val)
