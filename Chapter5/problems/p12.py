def bin_search(nums, first, last, number):
    if first > last:
        return False
    mid = (first + last)//2
    if nums[mid] == number:
        return True 
    elif number < nums[mid]:
        return bin_search(nums, first, mid-1, number)
    else:
        return bin_search(nums, mid+1, last, number)

def binary_search(nums, number):
    return bin_search(nums, 0, len(nums)-1, number)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))