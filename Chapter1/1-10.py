word_list = ["hello","world"]
list = []
for word in word_list:
    for i in word:
        list.append(i)

print(list)

sq_list = [x*x for x in range(1,11)]
print(sq_list)

sq_list = [x*x for x in range(1,11) if x%2 == 0]
print(sq_list)

wlist = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
print(wlist)