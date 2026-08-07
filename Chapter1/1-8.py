print (6 / 3) #float division
print (6 // 3) #integer division
print (6 ** 3) #6^3
print (6 % 3)

print (not (True and False)) #true

print (5 == 10)

mylist = [1,2,3,4]
biglist = mylist * 2 #creates a new list by copying the elements
checklist = [mylist] * 2 #creates a list with two references to mylist
mylist[2] = 10
print(biglist)
print(checklist)

#some list operations, note that lists in python are dynamic arrays

print("------------------------------------------")
mylist = [1,2,True,4]
mylist.append("world")
print(mylist)
mylist.insert(2, "wow")
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(2)
print(mylist)
mylist.sort()
print(mylist) #true == 1
mylist.append(1)
mylist.append(1)
print(mylist.count(1)) #true is also counted as 1
print(mylist)
print(mylist.remove(1)) #not a printable value i suspect (returns void)
print(mylist) #removes the first occurance of 1
del mylist[0]
print(mylist) #removes the first element of the list, similar to mylist.pop(0) but returns nothing
print(mylist.pop(1))

print(mylist[1:3])

print (list(range(1,20)))

name = "david"
print(name*2)
x = len(name)
print(x)

print(name.find('v'))
print(name.split('v')) # note that in python single and double quotes are interchangable

#name[0] = c -> this is invalid as strings are not mutable
#because change strings can be troublesome, cause issues with the hash table and also-
#if a = "hello" and b = "hello", a and b both point to the same address. changing b would cause errors (this is done for speed)

#tuples are immutable like strings

a = mylist #here mylist is a pointer to references, so if mylist changes, so does a
print(a)
mylist[0] = 4
print(a)

# a = mylist.copy() or a = mylist[:] will do the job of copying 

x = 10
b = x
x = 20
print(b)

#sets- sets are immutable 
print("---------------------------------")
myset = {3,5,6,'cat',False}
print (myset) #sorted ofcourse

#myset is immutable so it cant have a list in it

print(False in myset)
print("dog" in myset)

checkset = {False,'cat',3,5,6}

print(myset == checkset) #order doesnt matter in a set

#some set operations

yourset = {99,100,101}

print(myset.union(yourset))
#union- | intersection- & difference- - 

print('-----------------------------')

#dictionaries

capitals = {"Telengana":"hyderabad", "karnataka":"bangalore", "maharastra":"bombay"}

print(capitals["Telengana"])
print(capitals)
capitals["haryana"] = "gurugram"
print(capitals)
print(len(capitals))
for k in capitals:
    print(capitals[k],"is the capital of",k) #k are the keys and capitals[k] are the values

print(list(capitals.keys()))
print(list(capitals.values()))

print(list(capitals.items()))

print(capitals.get("karnataka"))