from timeit import Timer
import matplotlib.pyplot as plt
import random

nvals = []
tvals = []

for i in range (1_000_000, 50_000_001, 1_000_000):
    t = Timer(f"x[{i//2}]", "from __main__ import x, random")
    nvals.append(i)
    x = list(range(i))
    tvals.append(t.timeit(number = 1000))
    print(f"n = {i} timed")

nvals_scaled = [n / 1e6 for n in nvals] #millions
tvals_scaled = [t * 1e6 for t in tvals] #microseconds

plt.figure()
plt.plot(nvals, tvals)
plt.xlabel("n (millions)")
plt.ylabel("time (microseconds)")
plt.show()

'''
    fluctuations are between 1 and 1.8 microseconds which shows a constant nature
'''
