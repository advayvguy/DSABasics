def merge_sort(nums, first, last):
    if first < last:
        mid = (first + last)//2
        merge_sort(nums, first, mid)
        merge_sort(nums, mid+1, last)

        temp_arr = [0]*(last-first+1)
        i = first
        j = mid + 1
        k = 0
        while i <= mid and j <= last:
            if nums[i] >= nums[j]:
                temp_arr[k] = nums[j]
                j += 1
            elif nums[j] >= nums[i]:
                temp_arr[k] = nums[i]
                i += 1
            k += 1
        
        while i <= mid:
            temp_arr[k] = nums[i]
            i += 1
            k += 1
        
        while j <= last:
            temp_arr[k] = nums[j]
            j += 1
            k += 1
    
        for i in range(len(temp_arr)):
            nums[first + i] = temp_arr[i]

nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(nums,0,8)
print(nums)