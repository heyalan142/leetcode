def max_sub_string(s: str) -> str:
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j-1])
    return dp[0][-1]


if __name__ == '__main__':
    string = "bbbab"
    print(max_sub_string(string))


