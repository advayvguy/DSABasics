#two ways of finding sum to n 
import time

def sum_iterative(n):
    start = time.time()
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    end = time.time()
    return sum, end-start

def sum_formula(n):
    start = time.time()
    sum = int((n*(n+1))/2)
    end = time.time()
    return sum, end - start 

print("%d in %10.9lf secs" % sum_iterative(1000000000))
print("%d in %10.9lf secs" % sum_formula(1000000000), "<- significantly faster")

#we are also concerned about readability of the code

