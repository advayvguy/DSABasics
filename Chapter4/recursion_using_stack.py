from ADT import Stack

#we will use stack to convert an integer to a string of base 10

r_stack = Stack()

def convertor(num):
    while num > 0:
        r_stack.push(str(num%2))
        num = num//2

    return "".join(r_stack.pop() for _ in range(r_stack.size()))

print(convertor(100))
