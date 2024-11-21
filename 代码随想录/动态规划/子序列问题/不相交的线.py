def max_uncrossed_lines(A: list[int], B: list[int]) -> int:
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


if __name__ == '__main__':
    A = [1, 4, 2]
    B = [1, 2, 4]
    print(max_uncrossed_lines(A, B))
