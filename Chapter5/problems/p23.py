#median of 3 implementation of quick sort 
def median(nums, a, b, c):
    A, B, C = nums[a], nums[b], nums[c]
    if (A < B) != (A < C):
        return a
    if (B < A) != (B < C):
        return b
    return c

def partition(nums, first, last):
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

def q_sort_helper(nums, first, last):
    if first < last:
        split = partition(nums, first, last)
        q_sort_helper(nums, first, split-1)
        q_sort_helper(nums, split + 1, last)

def qsort(nums):
    q_sort_helper(nums, 0, len(nums) - 1) 

nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
qsort(nums)
print(nums)