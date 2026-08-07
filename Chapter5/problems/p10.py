import time
import random 

def seq_search(nums, number):
    start = time.perf_counter()
    for i in range(len(nums)):
        if nums[i] == number:
            break
    stop = time.perf_counter()
    return stop - start

def bin_search(nums, number):
    start = time.perf_counter()

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low+high)//2
        if nums[mid] == number:
            break
        elif nums[mid] > number:
            low = mid + 1
        else:
            high = mid - 1
    
    stop = time.perf_counter()

    return stop-start

lst = sorted(random.randint(1, 10000) for _ in range(1000000))

av_bin = 0
av_seq = 0
for i in range(100):
    choice = random.choice(lst)
    av_bin += bin_search(lst, choice)
    av_seq += seq_search(lst, choice)

print("sequential search- ", av_seq)
print("binary search- ", av_bin)