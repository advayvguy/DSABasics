'''
    In this problem, in addition to paranthesis matching, we also have to check the order in which the
    different paranthesis close.
    for example ([)] is not valid as the innermost left paranthesis should be the first one to close

    to solve this we pushed the paranthesis on the stack and while poping them we also checked if the type
    of the left and the right paranthesis matched.
'''

from stack import Stack 

def matches(s1, s2):
    left = "([{"
    right = ")]}"

    return left.index(s1) == right.index(s2)

def para_check(a):
    l = len(a)
    s = Stack()
    for i in range(l):
        if a[i] in "([{":
            s.push(a[i])
        else:
            if (s.is_empty()):
                return False
            else:
                check = matches(s.pop(), a[i])
                if check == 0:
                    return False
    
    if (s.is_empty()):
        return True
    else:
        return False 

print(para_check("{{([][])}()}"))
print(para_check("([)]"))
