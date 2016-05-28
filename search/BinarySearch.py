def binary_search(val, sorted_data):
    if len(sorted_data) <= 0:
        return -1
    mid = len(sorted_data) // 2
    if val < sorted_data[mid]:
        return binary_search(val, sorted_data[:mid])
    elif val > sorted_data[mid]:
        return binary_search(val, sorted_data[mid + 1:])
    else:
        return mid
