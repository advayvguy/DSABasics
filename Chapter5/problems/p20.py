import random, time

def shell_sort(a_list, division):
    sublist_count = len(a_list)//division
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(a_list, pos_start, sublist_count)
        sublist_count = sublist_count // division

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        cur_value = a_list[i]
        pos = i - gap
        while pos >= start and a_list[pos] > cur_value:
            a_list[pos+gap] = a_list[pos]
            pos -= gap
        a_list[pos+gap] = cur_value

def main():
    nums = [random.randint(1,10000) for _ in range(25)]
    i_start = 2
    for i in range(i_start, len(nums)):
        lst = nums.copy()
        start = time.perf_counter()
        shell_sort(lst, i)
        stop = time.perf_counter()
        print("gapsize- ",i," time- ",stop-start)

main()