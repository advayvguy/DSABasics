from timeit import Timer
import matplotlib.pyplot as plt
'''
    indexing a list is done in O(1) time
    -> every single element in a list is a pointer to an object
    -> indexing follows the algorithm-> address = base address + ( i * size of each element )

    append- O(1) if the address at the end of the list is free
    otherwise you may need a reallocation which may have some overhead O(n)
    python uses overallocation-
    4 -> 16 -> 32 -> ...
    so the number of reallocs arent as common

    concatination is O(k) where k is the size of the list being concatenated
    I am guessing this is because every single address needs a mapping 
'''

def test1():
    l = []
    for i in range (0,1000):
        l = l + [i] 

def test2():
    l = []
    for i in range(0,1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()","from __main__ import test1") #sets up a benchmark, we want to execute test1() which belongs to __main__
print(f"concatenation: {t1.timeit(number = 1000):15.2f} milliseconds") #executes the function in the benchmark 1000 times

t2 = Timer("test2()","from __main__ import test2")
print(f"appending: {t2.timeit(number = 1000):19.2f} milliseconds")

t3 = Timer("test3()","from __main__ import test3")
print(f"list comprehension: {t3.timeit(number = 1000):10.2f} milliseconds")

t4 = Timer("test4()","from __main__ import test4")
print(f"list range: {t4.timeit(number = 1000):18.2f} milliseconds")

'''
    algorithm analysis for the above functions:-

        test1():
            creation of [i] -> O(1)
            l + [i] -> copying all the elements of the list l and adding i to it -> O(k)
            doing this for 0 <= i < n -> O(n^) 
            time complexity is O(n^2)

        test2():
        python lists store the size of the list, so its easy to go to the end of the list as lists are contagious 
        address of next free space = address of the first element + size * size of pointer
            appending i -> O(1)
            doing this for 0 <= i < n -> O(n)
            time complexity is O(n)

        test3():
            iterates over 0,n and adds it all to the list
            time complexity = O(n) (but constant factors are smaller than that of append)

            this still runs faster than the append algorithm because there is lesser overhead.
            and also such list comprehensions are dealt by precompiled C code making it a little faster

        test4():
            time complexity - O(n)
            memory is preallocated to 1000 so no allocation overhead unlike test 2 and test 3
'''

'''
    some list operations:-

        pop- O(1)
        pop(i) = O(n)

        this is obvious because pop just pops out the last element of the list
        no rearrengement of the list is required, changing the size of the list is enough

        whereas in pop(i)-
            you pop the ith element of the list
            after that you have to change the index of each of the element
            every element after i needs an index conversion from k to k-1

        all list operations are quite straightforward apart from sort
        the fastest sorting algorithm is done in O(nlogn) time complexity
'''

#for example lets compare the time taken to pop the last vs the first element of a long array

pop_z = Timer("x.pop(0)","from __main__ import x")
pop = Timer("x.pop","from __main__ import x")

nvals = []
pop_z_vals = []
pop_vals = []

for i in range (100_000, 10_000_001, 100_000):
    x = list(range(i))
    pop_z_t = pop_z.timeit(number = 10)

    x = list(range(i))
    pop_t = pop.timeit(number = 10)

    nvals.append(i)
    pop_z_vals.append(pop_z_t)
    pop_vals.append(pop_t)

plt.plot(nvals, pop_z_vals, label = "pop(0)")
plt.plot(nvals, pop_vals, label = "pop()")

plt.xlabel("n (list size)")
plt.ylabel("time (seconds)")
plt.title("pop(0) vs pop() performance")

plt.show()
