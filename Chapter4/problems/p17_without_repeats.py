def knapsack(capacity, weights, values):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]

        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
        print(dp)

    return dp[capacity]

def main():
    weights = [2, 3, 4, 5, 9]
    values = [3, 4, 8, 8, 10]
    capacity = 6

    print(knapsack(capacity, weights, values))

main()