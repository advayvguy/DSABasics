from dequeue import Dequeue

def palindrome(word):
    
    queue = Dequeue()
    for i in word:
        queue.add_rear(i)

    while(queue.size() > 1):
        s1 = queue.remove_rear()
        s2 = queue.remove_front()
        if s1 != s2:
            return "is not a palindrome"

    return "is a palindrome"

print(palindrome("racecar"))
print(palindrome("advay"))
