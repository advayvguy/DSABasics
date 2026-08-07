import time 

def anagram_fast( s1,s2):
    start = time.time()
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    if (len(l1) != len(l2)):
        return "not an anagram"
    for i in range (0,len(l1)):
        if (l1[i] != l2[i]):
            return "not an anagram"
    end = time.time()
    return "is an anagram", end-start

def anagram_slow(s1,s2):
    start = time.time()
    if (len(s1) != len(s2)):
        return "not an anagram"
    
    l2 = list(s2)

    for i in range (0,len(s1)):
        found = False 
        for j in range (0,len(l2)):
            if s1[i] == l2[j]:
                l2.pop(j)
                found = True 
                break 
        if found == False:
            return "not an anagram"
    end = time.time()
    return "is an anagram", end-start

def anagram_best(s1,s2):
    start = time.time()
    c1 = [0]*26
    c2 = [0]*26
    for i in range (0, len(s1)):
        c1[ord(s1[i]) - ord("a")] += 1 #increment value of cell with index corresponding to alphabet number
        c2[ord(s2[i]) - ord("a")] += 1

    for i in range (0, 26):
        if (c1[i] != c2[i]):
            return "not an anagram"
    end = time.time()
    return "is an anagram", end-start

s1 = "abcdefghijklmnopqrstuvwxyz" * 40000
s2 = "zyxwvutsrqponmlkjihgfedcba" * 40000

print (anagram_fast(s1,s2))
print (anagram_slow(s1,s2))
print (anagram_best(s1,s2))

print (anagram_fast("hello","yello"))
print (anagram_slow("hello","yello"))
print (anagram_best("hello","yello"))
'''
    algorithm analyis-
    for the first algorithm:-
        non trivial time eaters-
        sort:- nlogn
        l2 = list(s2):- n 
        loop:- n

        T(n) = k(nlogn + n) ≈ nlogn (for large numbers)
        O(nlogn)

    for the second algorithm:-
        non trivial time eaters-
        looping:-
        for the first element:- n 
        first the second element:- n-1 
        .
        .
        .
        for the nth element:- 1
        time complexity = n + n-1 + n-2 + ... + 1
                        = ∑i = n(n+1)/2
                        = n^2/2 + n/2
        O(n^2)

    for a brute force style algorithm:- 
        we find out all the anagrams of the string and then compare it to the target string
        total number of possible anagrams = n!
        therefore
        time complextiy is O(n!)

    for the best anagram method:-
        non trivial time eaters:-
            looping over the list once- n 
            looping over c1 and c2- 26 
            total time = k(n + 26)

        the time complexity is O(n) for this algorithm

    output analysis for the given inputs-
        ('is an anagram', 0.03946113586425781)
        ('is an anagram', 4.214015960693359)
        ('is an anagram', 0.03798222541809082)
        

    FUN FACT- 

    list.sort() uses a time sort implementation in C, so that code is compiled code.
    it runs faster than the loop overheads in python hence why nlogn in this case performs slightly better
    than n for large inputs

'''
