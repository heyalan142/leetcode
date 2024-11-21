class Solution:

    def solve_queens(self, n: int) -> list[list[str]]:
        result = []  # 存储最终结果的二维字符串数组
        chessboard = ['.' * n for _ in range(n)]  # 初始化棋盘
        self.backtracking(n, 0, chessboard, result)  # 回溯求解
        return result

    def backtracking(self, n: int, row: int, chessboard: list[str], result: list[list[str]]) -> None:
        if row == n:
            result.append(chessboard[:])
        for col in range(n):
            if self.is_valid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col + 1:]  # 放置皇后
                self.backtracking(n, row + 1, chessboard, result)  # 递归到下一行
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col + 1:]  # 回溯，撤销当前位置的皇后

    def is_valid(self, row: int, col: int, chessboard: list[str]) -> bool:
        # 检查列
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False  # 当前列已经存在皇后，不合法

        # 检查 45 度角是否有皇后
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法


if __name__ == '__main__':
    print(Solution().solve_queens(4))
