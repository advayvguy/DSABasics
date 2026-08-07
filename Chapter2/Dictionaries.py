'''
    dictionaries are implemented in python by a hashmap
    and luckily I know how a hashmap works :)
'''

'''
    copy- O(n)
    get_item- O(1)
    set_item- O(1)
    delete_item- O(1)
    contains (in)- O(1)
    iteration- O(n)
'''

import matplotlib.pyplot as plt
from timeit import Timer
import random #random number generator- more or less follows a uniform distribution

n_vals  = []
l_times = []
d_times = []

for i in range (10_000,1_000_001,20_000):
    t = Timer(f"random.randrange({i}) in x", "from __main__ import random,x")
    
    x = list(range(i))
    l_times.append(t.timeit(number = 1000))

    x = {j:None for j in range (i)}
    d_times.append(t.timeit(number = 1000))

    n_vals.append(i)

    print(f"n = {i} timed")

plt.figure()
plt.plot(n_vals, l_times, label = "searching in list")
plt.plot(n_vals, d_times, label = "searching in hashmap")
plt.xlabel("n")
plt.ylabel("time")
plt.show()
