def different_sub_seq(source, target) -> int:
    len_s = len(source)
    len_t = len(target)

    i = 0
    j = 0

    dp = []

    while i < len_s and j < len_t:
        if source[i] == target[j]:
            dp[i][j] = dp[i - 1][j] + 1
        else:
            dp[i][j] = dp[i - 1][j]
