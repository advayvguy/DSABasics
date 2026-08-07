from ADT import Queue


def radix_sort(array):
    mainbin = Queue()
    small_bins = [Queue() for i in range(10)] #radix sort of base 10

    for item in array:
        mainbin.enqueue(item)

    base = 0
    output_arr = []
    while(1):
        while(not mainbin.is_empty()):
            item = mainbin.dequeue()
            small_bins[(item//(10**base))%10].enqueue(item)

        if small_bins[0].size() == len(array):
            while(not small_bins[0].is_empty()):
                output_arr.append(small_bins[0].dequeue())
            break

        for bin in small_bins:
            while(not bin.is_empty()):
                mainbin.enqueue(bin.dequeue())
        base = base + 1

    return output_arr

print(radix_sort([3,7,8,17,0,2,4,6,10]))
