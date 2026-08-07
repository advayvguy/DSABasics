import time, random

def bin_search_slice(nums, number):
    mid = len(nums)//2
    if nums[mid] == number:
        return 
    if number > nums[mid]:
        bin_search_slice(nums[mid+1:], number)
    else:
        bin_search_slice(nums[:mid], number)

def bin_search_rec(nums, number):
    start = time.perf_counter()
    bin_search_slice(nums, number)
    stop = time.perf_counter()
    return stop-start

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
av_bins = 0
for i in range(100):
    choice = random.choice(lst)
    av_bin += bin_search(lst, choice)
    av_bins += bin_search_rec(lst, choice)

print("using slice- ", av_bins)
print("without using slice- ", av_bin)