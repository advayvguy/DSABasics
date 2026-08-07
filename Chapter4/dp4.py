#cleaner version of dp3 i think

def count_coins(coin_list, target):
    dp = [i for i in range(target+1)]
    for coin in coin_list:
        for i in range(coin, target+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[target]

def main():
    coins = [1,5,10,21,25]
    amt = 63
    count_coins(coins, amt)
    print(count_coins(coins, amt))

main()