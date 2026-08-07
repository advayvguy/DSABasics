'''
    implementing a stack in python
'''

class Stack:
    def __init__(self):
        self._items = [] #maybe we put the '_' before items to indicate that its private

    def is_empty(self):
        return not len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1] #i didnt know this was a thing?

    def size(self):
        return len(self._items)

def rev_string(my_str):
    s = Stack() #O(1)
    reversed = []  #O(1)
    for i in range(0,len(my_str)):
        s.push(my_str[i])  # O(n)
    while not s.is_empty():
        reversed.append(s.pop()) # O(n)
    return "".join(reversed) #  O(n)

def test(my_str,expected_str):
    check = rev_string(my_str)
    if (check == expected_str):
        print("Pass")
    else:
        print("Fail incorrect output:- %s",check)

test("apple","elppa")
test("1234567890","0987654321")

'''
    push and pop operations will take O(1) time complexity
'''
