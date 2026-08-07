from ADT import Node, UnorderedList
from ADT import Node, UnorderedList
import random
import time

print("---------------------------------")
testlist = [i for i in range(10000)]
testlinkedlist = UnorderedList()
for i in range(10000):
    testlinkedlist.add(i)

#test to search for an element in the list vs linkedlist
#list-
tlist = 0
for i in range(20000):
    rand = random.randrange(10000)
    start = time.time()
    if rand in testlist:
        end = time.time()
        tlist = tlist + end - start

print(f"searching in a list- {tlist} seconds")

#linkedlist
tlinkedlist = 0
for i in range(20000):
    rand = random.randrange(10000)
    start = time.time()
    if testlinkedlist.search(rand):
        end = time.time()
        tlinkedlist = tlinkedlist + end - start

print(f"searching in a linked list- {tlinkedlist} seconds")

print("---------------------------------")
#adding an element in a list vs linked list
#list-

tlist = 0
for i in range(10001,20001):
    start = time.time()
    testlist.append(i)
    end = time.time()
    tlist = tlist + end - start

print(f"adding elements to a list- {tlist} seconds")

#linkedlist- 

tlinkedlist = 0
for i in range(10001, 20001):
    start = time.time()
    testlinkedlist.add(i)
    end = time.time()
    tlinkedlist = tlinkedlist + end - start

print(f"adding elements to a linked list- {tlinkedlist} seconds")

print("---------------------------------")

#removing elements from a list vs linkedlist

tlist = 0
for i in range(20001, 10001, -1):
    start = time.time()
    testlist.pop()
    end = time.time()
    tlist = tlist + end - start

print(f"removing elements from a list- {tlist} seconds")

tlinkedlist = 0
for i in range(20000, 10000, -1):
    start = time.time()
    testlinkedlist.remove(i)
    end = time.time()
    tlinkedlist = tlinkedlist + end - start

print(f"adding elements on the linked list- {tlinkedlist} seconds")
print("---------------------------------")
import random
import time

print("---------------------------------")
testlist = [i for i in range(10000)]
testlinkedlist = UnorderedList()
for i in range(10000):
    testlinkedlist.add(i)

#test to search for an element in the list vs linkedlist
#list-
tlist = 0
for i in range(20000):
    rand = random.randrange(10000)
    start = time.time()
    if rand in testlist:
        end = time.time()
        tlist = tlist + end - start

print(f"searching in a list- {tlist} seconds")

#linkedlist
tlinkedlist = 0
for i in range(20000):
    rand = random.randrange(10000)
    start = time.time()
    if testlinkedlist.search(rand):
        end = time.time()
        tlinkedlist = tlinkedlist + end - start

print(f"searching in a linked list- {tlinkedlist} seconds")

print("---------------------------------")
#adding an element in a list vs linked list
#list-

tlist = 0
for i in range(10001,20001):
    start = time.time()
    testlist.append(i)
    end = time.time()
    tlist = tlist + end - start

print(f"adding elements to a list- {tlist} seconds")

#linkedlist- 

tlinkedlist = 0
for i in range(10001, 20001):
    start = time.time()
    testlinkedlist.add(i)
    end = time.time()
    tlinkedlist = tlinkedlist + end - start

print(f"adding elements to a linked list- {tlinkedlist} seconds")

print("---------------------------------")

#removing elements from a list vs linkedlist

tlist = 0
for i in range(20001, 10001, -1):
    start = time.time()
    testlist.pop()
    end = time.time()
    tlist = tlist + end - start

print(f"removing elements from a list- {tlist} seconds")

tlinkedlist = 0
for i in range(20000, 10000, -1):
    start = time.time()
    testlinkedlist.remove(i)
    end = time.time()
    tlinkedlist = tlinkedlist + end - start

print(f"adding elements on the linked list- {tlinkedlist} seconds")
print("---------------------------------")
