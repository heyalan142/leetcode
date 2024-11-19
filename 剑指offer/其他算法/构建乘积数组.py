class Solution:
    def multiply(self, A: list[int]) -> list[int]:
        B = [1 for _ in range(len(A))]
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        # 关键代码：再乘右边，从右到左
        for i in reversed(range(len(A))):
            B[i] *= temp
            temp *= A[i]
        return B


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    val = Solution().multiply(A)
    print(val)
