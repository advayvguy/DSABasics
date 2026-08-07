#modified string hash function to battle anagrams
#note that the hash function should be simple, preferably O(k) otherwise the purpose of hashing is defeated

def hash_str(a_string, table_size):
    sum = 0
    for i in range(len(a_string)):
        sum += ord(a_string[i])*(i+1)
    return sum%table_size

print(hash_str("cat",11))