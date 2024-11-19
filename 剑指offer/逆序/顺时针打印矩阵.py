class Solution:

    def printMatrix(self, matrix) -> list():
        results = []
        rowStart = 0
        colStart = 0
        rowEnd = len(matrix) - 1
        firstRow = matrix[rowStart]
        colEnd = len(firstRow) - 1
        while rowStart < rowEnd and colStart < colEnd:
            for j in range(colStart, colEnd + 1):
                results.append(matrix[rowStart][j])
            results.pop()
            for i in range(rowStart, rowEnd + 1):
                results.append(matrix[i][colEnd])
            results.pop()
            for j in range(colEnd, colStart - 1, -1):
                results.append(matrix[rowEnd][j])
            results.pop()
            for i in range(rowEnd, rowStart - 1, -1):
                results.append(matrix[i][colStart])
            results.pop()
            rowStart += 1
            rowEnd -= 1
            colStart += 1
            colEnd -= 1

        if rowStart == rowEnd and colStart == colEnd:
            results.append(matrix[rowStart][colStart])
        elif rowStart == rowEnd:
            for j in range(colStart, colEnd + 1):
                results.append(matrix[rowStart][j])
        elif colStart == colEnd:
            for i in range(rowStart, rowEnd + 1):
                results.append(matrix[i][colStart])
        return results


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    result = Solution().printMatrix(matrix)
    print(result)
