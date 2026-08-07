from stack import Stack

def para_check(a):
    s = Stack()
    l = len(a)
    for i in range(l):
        if (a[i] == '('):
            s.push(1)
        if (a[i] == ')'):
            if (s.is_empty()):
                return False
            else:
                s.pop()

    if (s.is_empty()):
        return True
    else:
        return False

print(para_check("((((((())"))
print(para_check("(()((())()))"))
