from ADT import Stack

n = 17
s = Stack()
while (n > 0):
    s.push(n%2)
    n = n//2
l = []
while not s.is_empty():
    l.append(str(s.pop()))

print("".join(l))
