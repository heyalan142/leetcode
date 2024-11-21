def max_bag_value(weights: [int], values: [int], bag_weight: int) -> int:
    dp = [[0] * (bag_weight + 1) for _ in range(len(weights))]
    for i in range(0, len(weights)):
        dp[i][0] = 0
    for j in range(1, weights[0]):
        dp[0][j] = 0
    for j in range(weights[0], bag_weight + 1):
        dp[0][j] = values[0]
    for j in range(0, bag_weight + 1):
        for i in range(1, len(weights)):
            if j > weights[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i]);
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(weights) - 1][bag_weight]


if __name__ == '__main__':
    weights = [1, 3, 4]
    values = [15, 20, 30]
    bag_weight = 4
    print(max_bag_value(weights, values, bag_weight))
