def max_length_of_sublist(numsA: [int], numsB: [int]) -> int:
    if len(numsA) <= 0:
        return 0
    dp = [[0] * (len(numsB) + 1) for _ in range(len(numsA) + 1)]
    result = 0
    for i in range(1, len(numsA) + 1):
        for j in range(1, len(numsB) + 1):
            if numsA[i - 1] == numsB[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > result:
                result = dp[i][j]
    return result


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]

    print(max_length_of_sublist(A, B))
