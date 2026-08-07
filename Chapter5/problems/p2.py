def hash_string(word, bucket_size):
    sum = 0
    for i in range(len(word)):
        sum += ord(word[i])*(i+1)
    return sum%bucket_size

print(hash_string("advay", 11))