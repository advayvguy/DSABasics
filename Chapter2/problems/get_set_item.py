from timeit import Timer
import matplotlib.pyplot as plt

nvals = []
tvals1 = []
tvals2 = []

for i in range (1_000_000, 50_000_001, 1_000_000):
    nvals.append(i)
    t1 = Timer(f"x[{i//2}] = \"hello\"", "from __main__ import x")
    t2 = Timer(f"x[{i//2}]", "from __main__ import x")
    x = {j:None for j in range(i)}
    tvals1.append(t1.timeit(number = 1000))
    tvals2.append(t2.timeit(number = 1000))
    print(f"n = {i} timed")
    

nvals_scaled = [n / 1e6 for n in nvals] #millions
tvals1_scaled = [t * 1e6 for t in tvals1] #microseconds
tvals2_scaled = [t * 1e6 for t in tvals2] #microseconds

plt.figure()
plt.plot(nvals, tvals1, label= "set item")
plt.plot(nvals,tvals2, label = "get item")
plt.xlabel("n (millions)")
plt.ylabel("time (microseconds)")
plt.show()

'''
    its evident that both of the graphs are constant time graphs
'''
