def main():
    from_str = "algorithm"
    to_str = "alligator"
    rows = len(to_str) + 1
    cols = len(from_str) + 1

    dp = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        dp[i][0] = i*20
    for i in range(cols):
        dp[0][i] = i*20

    for i in range(1,rows):
        for j in range(1, cols):
            if from_str[j-1] == to_str[i-1]:
                dp[i][j] = dp[i-1][j-1] + 5
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 20

    print(dp[rows-1][cols-1])

main()