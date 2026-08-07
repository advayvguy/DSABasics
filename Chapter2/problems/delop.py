from timeit import Timer
import matplotlib.pyplot as plt

nvals = []
tvals0 = []
tvals1 = []
tvals2 = []

for i in range (1_000_000, 50_000_001, 1_000_000):
    nvals.append(i)
    t0 = Timer(f"del x[0]", "from __main__ import x")
    t1 = Timer(f"del x[{i//2}]", "from __main__ import x")
    t2 = Timer(f"del x[{i//2}]", "from __main__ import x")
    x = list(range(i))
    tvals0.append(t0.timeit(number = 1))
    x = list(range(i))
    tvals1.append(t1.timeit(number = 1))
    x = {j:None for j in range(i)}
    tvals2.append(t2.timeit(number = 1))
    print(f"n = {i} timed")
    

nvals_scaled = [n / 1e6 for n in nvals] #millions
tvals1_scaled = [t * 1e6 for t in tvals1] #microseconds
tvals2_scaled = [t * 1e6 for t in tvals2] #microseconds
tvals0_scaled = [t * 1e6 for t in tvals0] #microseconds

plt.figure()
plt.plot(nvals, tvals0)
plt.plot(nvals, tvals1)
plt.plot(nvals, tvals2)
plt.xlabel("n (millions)")
plt.ylabel("time (microseconds)")
plt.show()

'''
    clearly evident that the hashtable case is O(1) and the list case is O(n)
    case 1:- O(n)
    case 2:- O(n/2)
    case 3:- O(1) -> in a hash table you are not pushing any elements backwards by removing stuff from middle
'''
