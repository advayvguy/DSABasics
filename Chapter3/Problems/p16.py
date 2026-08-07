from ADT import Queue
import random

name_list = ["Advay","Nimish","Soham","Suraj","Satyaki","Devansh","Suryansh","Pratyask","Divyam"]
line = Queue()
for name in name_list:
    line.enqueue(name)

for i in range(random.randrange(1000)):
    out = line.dequeue()
    line.enqueue(out)

print(line.peek())
