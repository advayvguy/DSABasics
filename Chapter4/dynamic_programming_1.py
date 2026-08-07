#highly inefficient program 

def num_coins(change, value):
    if value in change:
        return 1
    min = float("inf") 
    for coin in change:
        if value >= coin:
            roots = num_coins(change, value - coin)
            if min > 1 + roots:
                min = 1 + roots
    return min

print(num_coins([1,5,10,25,21], 3))        