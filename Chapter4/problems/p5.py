def reverse(l, first, last):
    if first >= last:
        return l
    keep = l[first]
    l[first] = l[last]
    l[last] = keep
    return reverse(l, first + 1, last - 1)

print(reverse(list("racecar"), 0, 6))

