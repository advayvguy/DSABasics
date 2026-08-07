#this technique is called caching, we still havent tapped on dynamic programming
#caching- faster programs at an expense of storing known results

def num_coins(currency, change, known_results):
    if change in currency:
        known_results[change] = 1
        return 1
    if known_results[change] > 0:
        return known_results[change]
    min = float("inf")
    for coin in [c for c in currency if c < change]:
            roots = num_coins(currency, change - coin, known_results)
            if min > roots + 1:
                min = roots + 1
            known_results[change] = min
    return min 

print(num_coins([1,5,10,25], 163, [0]*164))  