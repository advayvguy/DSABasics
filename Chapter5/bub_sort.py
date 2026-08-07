def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                a = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = a

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)