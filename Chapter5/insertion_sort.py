def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_value = a_list[i]
        pos = i - 1
        while pos >= 0 and a_list[pos] > cur_value:
            a_list[pos+1] = a_list[pos]
            pos -= 1
        a_list[pos+1] = cur_value

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)