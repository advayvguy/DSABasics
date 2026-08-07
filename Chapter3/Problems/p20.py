from ADT import Deque

def ispalindrome(input):
    token_list = []
    palcheck = Deque()

    for ch in input:
        if ch != ' ' and ch != '\t':
            token_list.append(ch)

    for token in token_list:
        palcheck.add_rear(token)

    while (palcheck.size() > 1):
        s1 = palcheck.remove_rear()
        s2 = palcheck.remove_front()
        if s1 != s2:
            return False

    return True

print(ispalindrome("RACE    CAR"))
