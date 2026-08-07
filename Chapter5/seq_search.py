def seq_search(nums, num):
    pos = 0
    while pos < len(nums):
        if nums[pos] == num:
            return True
        pos += 1
    return False

nums = [1,2,4,5,6,10,9,7,32]

print(seq_search(nums, 3))
print(seq_search(nums, 32))