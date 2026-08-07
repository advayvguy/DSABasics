def make_change(change_list, amount, min_coins):
    for cents in range(amount + 1):
        min_change = cents
        for j in [c for c in change_list if c <= cents]:
            if min_coins[cents - j] + 1 < min_change:
                min_change = min_coins[cents-j] + 1
        min_coins[cents] = min_change

amt = 63
change_list = [1,5,10,21,25]
min_coins = [0]*(amt+1)
make_change(change_list, amt, min_coins)
print("change - coins")
for i in range(amt + 1):
    print(f"{i:^6} - {min_coins[i]:^5}")