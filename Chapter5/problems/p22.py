#quicksort using partition limits
import random, time

def insertion_sort(a_list, first, last):
    for i in range(first + 1, last + 1):
        cur_value = a_list[i]
        pos = i - 1
        while pos >= first and a_list[pos] > cur_value:
            a_list[pos+1] = a_list[pos]
            pos -= 1
        a_list[pos+1] = cur_value

def qsort_partition(nums, partition_limit):
    qsort_helper_partition(nums, 0, len(nums)-1, partition_limit)

def qsort(nums):
    qsort_helper(nums, 0, len(nums)-1)

def qsort_helper(nums, first, last):
    if first < last:
        split = partition(nums, first, last)
        qsort_helper(nums, first, split - 1)
        qsort_helper(nums, split + 1, last)

def qsort_helper_partition(nums, first, last, partition_limit):
    if first < last and (last-first+1) > partition_limit:
        split = partition(nums, first, last)
        qsort_helper_partition(nums, first, split - 1, partition_limit)
        qsort_helper_partition(nums, split + 1, last, partition_limit)
    elif (last - first + 1) <= partition_limit:
        insertion_sort(nums, first, last)

def partition(nums, first, last):
    pivot = nums[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and nums[left_mark] <= pivot:
            left_mark = left_mark + 1
        while left_mark <= right_mark and nums[right_mark] >= pivot:
            right_mark = right_mark - 1
        if left_mark > right_mark:
            done = True
        else:
            nums[left_mark], nums[right_mark] = nums[right_mark], nums[left_mark]

    nums[first], nums[right_mark] = nums[right_mark], nums[first]
    return right_mark

def median(nums, a, b, c):
    A, B, C = nums[a], nums[b], nums[c]
    if (A < B) != (A < C):
        return a
    if (B < A) != (B < C):
        return b
    return c

def partition3(nums, first, last):
    p_index = median(nums, first, (first+last)//2, last)
    pivot = nums[p_index]
    nums[first], nums[p_index] = nums[p_index], nums[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and nums[left_mark] <= pivot :
            left_mark += 1
        while left_mark <= right_mark and nums[right_mark] >= pivot:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            nums[left_mark], nums[right_mark] = nums[right_mark], nums[left_mark]
    
    nums[right_mark], nums[first] = nums[first], nums[right_mark]
    return right_mark

def q_sort_helper3(nums, first, last):
    if first < last:
        split = partition3(nums, first, last)
        q_sort_helper3(nums, first, split-1)
        q_sort_helper3(nums, split + 1, last)

def qsort_median(nums):
    q_sort_helper3(nums, 0, len(nums) - 1)       
    
def main():
    qsp_time = 0
    qs_time = 0
    qsm_time = 0

    for i in range(100):
        lst = [_ for _ in range(200)]

        nums = lst.copy()
        start = time.perf_counter()
        qsort(nums)
        stop = time.perf_counter()
        qs_time += stop - start

        nums = lst.copy()
        start = time.perf_counter()
        qsort_partition(nums, 16)
        stop = time.perf_counter()
        qsp_time += stop - start

        nums = lst.copy()
        start = time.perf_counter()
        qsort_median(nums)
        stop = time.perf_counter()
        qsm_time += stop - start

    print("quick sort-                         ", qs_time)
    print("quick sort with partition limit 16- ", qsp_time)
    print("quick sort with median of 3-        ", qsm_time) #median of 3 as expected is much faster

main()