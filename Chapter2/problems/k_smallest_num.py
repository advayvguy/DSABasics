import time 
import random
from timeit import Timer 
import matplotlib.pyplot as plt 

def sorting(x,k):
    x.sort()
    y = x[k-1]
    return y

def fastest(x,k):
    size = len(x)
    if k >= size:
        return "k is greater than len(x)"
    
    p = x[size//2]
    lows = [i for i in x if i < p]
    highs = [i for i in x if i > p]
    equals = [i for i in x if i == p]

    size_lows = len(lows)
    size_highs = len(highs)
    size_equals = len(equals)
    
    if k < size_lows:
        return fastest(lows,k)
    elif k < size_lows + size_equals:
        return p
    else:
        return fastest(highs, k - size_lows - size_equals)

def fast_algo(x,k):
    return fastest(x,k-1)

nvals = []
tf_vals = []
ts_vals = []

for i in range (1_000, 100_000, 1_000):
    lst = [random.randrange(i) for j in range(i)]
    k = random.randrange(i)
    tf = Timer(f"fast_algo({lst},{k})","from __main__ import fast_algo")
    ts = Timer(f"sorting({lst},{k})", "from __main__ import sorting")
    nvals.append(i)
    tf_vals.append(tf.timeit(number = 100))
    ts_vals.append(ts.timeit(number = 100))
    print(f"n = {i} timed")

plt.figure()
plt.plot(nvals, tf_vals)
plt.plot(nvals, ts_vals)
plt.xlabel("size of list")
plt.ylabel("time")
plt.show()

'''
    time complexity of the fast algorithm is O(nlogm) i think
    i dont think you can get it to be linear, this function has lots of devitions especially for high n values
    O(n) is best case
    further study of the fast algorithm is required. Ill get back to it later
'''
