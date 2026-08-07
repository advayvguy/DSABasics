#this performs better if the list is already sorted, avoids the O(n^2) worst case since the partition is equal on both sides

def partition(nums, first, last):
    pivot = nums[(first + last)//2]
    nums[first], nums[(first + last)//2] = nums[(first+last)//2], nums[first]
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