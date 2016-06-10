"""
O(n + k)
"""
COUNTING_SORT_MAX = 100000


def counting_sort(data, start=0, end=COUNTING_SORT_MAX):
    count = [0] * (end - start + 1)
    result = [0] * len(data)
    # k
    for value in data:
        count[value] += 1
    # n
    for i in range(start + 1, end):
        count[i] += count[i - 1]
    # k
    for value in reversed(data):
        result[count[value] - 1] = value
        count[value] -= 1
    return result
