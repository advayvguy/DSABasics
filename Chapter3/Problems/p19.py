from ADT import Stack

def paramax(array):
    
    s = Stack()
    for i in array:
        if i == '<':
            s.push(1)
        elif i == '>':
            if (s.is_empty()):
                return False
            s.pop()

    if (not s.is_empty()): 
        return False

    return True

array = input().split()
print(paramax(array))
