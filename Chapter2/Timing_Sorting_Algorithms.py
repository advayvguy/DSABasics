import matplotlib.pyplot as plt
from timeit import Timer

n_vals = []
tq_vals = []
tb_vals = []
N = 0

t_qsort = Timer("qsort()","from __main__ import qsort")
t_bubsort = Timer("bubsort()", "from __main__ import bubsort")

def qsort():
    x = list(range(N,0,-1))
    x.sort()

def bubsort():
    x = list(range(N,0,-1))
    for i in range(N):
        for j in range (0, N-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    
for i in range (100, 5_000, 100):
    N = i
    n_vals.append(i)
    tq_vals.append(t_qsort.timeit(number = 10))
    tb_vals.append(t_bubsort.timeit(number = 10))
    print (f"n = {i} timed")

plt.figure()
plt.plot(n_vals, tq_vals)
plt.xlabel("n (list size)")
plt.ylabel("time (seconds)")
plt.title("time complexity of quicksort algorithm")
plt.show()

plt.figure()
plt.plot(n_vals, tb_vals)
plt.xlabel("n (list size)")
plt.ylabel("time (seconds)")
plt.title("time complexity of a bubsort algorithm")
plt.show()
