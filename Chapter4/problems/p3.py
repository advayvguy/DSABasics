def make_change(amt, min_coins, change_list):
    for cents in range(amt + 1):
        num_coins = cents
        for j in [c for c in change_list if c <= cents]:
            if min_coins[cents - j] + 1 < num_coins:
                num_coins = min_coins[cents - j] + 1
        min_coins[cents] = num_coins
    return min_coins[amt]

amt = 33
min_coins = [0]*(amt + 1)
change_list = [1,5,8,10,25]
print(make_change(amt, min_coins, change_list))