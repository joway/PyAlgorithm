def binary_search(val, sorted_data):
    length = len(sorted_data)
    # [start, stop]
    start = 0
    stop = length - 1
    while start <= stop:
        mid = (stop + start) // 2
        if sorted_data[mid] < val:
            start = mid + 1
        elif sorted_data[mid] > val:
            stop = mid - 1
        else:
            return mid
    return -1

