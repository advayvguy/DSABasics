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

nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(nums)
print(nums)