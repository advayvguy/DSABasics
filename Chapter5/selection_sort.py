#since selection sort has fewer exchanges that a bubble sort, it is generally faster

def selection_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        max = 0
        for j in range(1,i+1):
            if nums[j] > nums[max]:
                max = j
        temp = nums[max]
        nums[max] = nums[i]
        nums[i] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)
        