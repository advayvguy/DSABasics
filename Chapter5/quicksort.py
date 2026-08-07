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
    
nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
qsort(nums)
print(nums)