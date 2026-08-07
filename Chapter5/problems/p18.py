import time, random

def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                a = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = a

def selection_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        max = 0
        for j in range(1,i+1):
            if nums[j] > nums[max]:
                max = j
        temp = nums[max]
        nums[max] = nums[i]
        nums[i] = temp

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_value = a_list[i]
        pos = i - 1
        while pos >= 0 and a_list[pos] > cur_value:
            a_list[pos+1] = a_list[pos]
            pos -= 1
        a_list[pos+1] = cur_value

def shell_sort(a_list):
    sublist_count = len(a_list)//2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(a_list, pos_start, sublist_count)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        cur_value = a_list[i]
        pos = i - gap
        while pos >= start and a_list[pos] > cur_value:
            a_list[pos+gap] = a_list[pos]
            pos -= gap
        a_list[pos+gap] = cur_value

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        
        i = 0
        j = 0
        k = 0
        while k < len(nums):
            if i == len(left_half): #if i reaches the end of the left half, we just fill the rest up with elements of the right half
                nums[k] = right_half[j]
                j = j + 1
            elif j == len(right_half): #if j reaches the end of the left half, we just fill the rest up with elements of the left half
                nums[k] = left_half[i]
                i = i + 1  
            elif left_half[i] <= right_half[j]:
                nums[k] = left_half[i]
                i = i + 1
            else:
                nums[k] = right_half[j]
                j = j + 1
            k = k + 1

def qsort(nums):
    qsort_helper(nums, 0, len(nums)-1)

def qsort_helper(nums, first, last):
    if first < last:
        split = partition(nums, first, last)
        qsort_helper(nums, first, split - 1)
        qsort_helper(nums, split + 1, last)

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

def main():
    bub_time = 0
    sel_time = 0
    ins_time = 0
    she_time = 0
    mer_time = 0
    qui_time = 0
    for i in range (100):
        lst = [random.randint(1,100000) for _ in range(1000)]

        start = time.perf_counter()
        for_sort = lst.copy()
        bubble_sort(for_sort)
        stop = time.perf_counter()
        bub_time += stop - start

        start = time.perf_counter()
        for_sort = lst.copy()
        selection_sort(for_sort)
        stop = time.perf_counter()
        sel_time += stop - start

        start = time.perf_counter()
        for_sort = lst.copy()
        insertion_sort(for_sort)
        stop = time.perf_counter()
        ins_time += stop - start

        start = time.perf_counter()
        for_sort = lst.copy()
        shell_sort(for_sort)
        stop = time.perf_counter()
        she_time += stop - start

        start = time.perf_counter()
        for_sort = lst.copy()
        merge_sort(for_sort)
        stop = time.perf_counter()
        mer_time += stop - start

        start = time.perf_counter()
        for_sort = lst.copy()
        qsort(for_sort)
        stop = time.perf_counter()
        qui_time += stop - start

    print("bubble sort-", bub_time)
    print("selection sort-", sel_time)
    print("insertion sort-", ins_time)
    print("shell sort-", she_time)
    print("merge sort-", mer_time)
    print("quick sort-", qui_time)

main() 