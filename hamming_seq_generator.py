import random 
a = [random.randrange(0,2) for i in range(16)]
b = 0
for i in range(16):
    if a[i]:
        b ^= i
if (b & 1):
    a[1] ^= 1
if (b & 2):
    a[2] ^= 1
if (b & 4):
    a[4] ^= 1
if (b & 8):
    a[8] ^= 1
print(a)

