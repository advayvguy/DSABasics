def hash_function(number, b_size, table):
    hash = number%b_size
    i = 1
    while table[hash] is not None:
        hash = (number + i*i)%hash
        i += 1
    return hash
