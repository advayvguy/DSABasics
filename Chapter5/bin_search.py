def bin_search_rec(nums, first, last, num):
    mid = (first + last)//2
    if num == nums[mid]:
        return True
    elif first >= last:
        return False
    elif num > nums[mid]:
        return bin_search_rec(nums, mid+1, last, num)
    else:
        return bin_search_rec(nums, first, mid-1, num)
    
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(bin_search_rec(test_list, 0, len(test_list)-1, 3))
print(bin_search_rec(test_list, 0, len(test_list)-1, 13))