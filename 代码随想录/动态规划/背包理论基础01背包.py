def max_bag_value(values: list[int], weights: list[int], bag_weight: int) -> int:
    dp = [[0] * (bag_weight + 1) for _ in range(len(values))]
    for j in range(weights[0], bag_weight + 1):
        dp[0][j] = values[0]
    for j in range(1, bag_weight + 1):
        for i in range(1, len(values)):
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weights[i]] + values[i])
    return dp[len(values) - 1][bag_weight]


if __name__ == "__main__":
    values = [15, 20, 30]
    weights = [1, 3, 4]
    bag_weight = 4
    print(max_bag_value(values, weights, bag_weight))
