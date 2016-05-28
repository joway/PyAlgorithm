import copy


def insert_sort(data):
    result = copy.deepcopy(data)
    for i in range(1, len(result)):
        key = result[i]
        left = i - 1
        while left >= 0 and result[left] > key:
            result[left + 1] = result[left]
            left -= 1
        result[left + 1] = key
    return result
