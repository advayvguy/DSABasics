import time 
#two python functions to find the shortest element of the list

def longscanner(a):
    start = time.time()
    for i in range (0,len(a)):
        for j in range (0,len(a)):
            if (a[j] > a[i]):
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    end = time.time()
    return a[0], end-start

def shortscanner(a):
    min = a[0]
    start = time.time()
    for i in range (0, len(a)):
        if (a[i] < min):
            min = a[i]
    end = time.time()
    return min, end-start

print (shortscanner([2,3,4,5,1,3,2,3,10]))
print (longscanner([2,3,4,5,1,3,2,3,10]))
