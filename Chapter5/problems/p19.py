def bubble_sort(nums):
    left_mark = 0
    right_mark = len(nums)-1
    while left_mark < right_mark:
        for i in range(left_mark, right_mark):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
        right_mark -= 1
        for i in range(right_mark, left_mark, -1):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1],nums[i]
        left_mark += 1

nums = [5,4,3,2,1]
bubble_sort(nums)
print(nums)