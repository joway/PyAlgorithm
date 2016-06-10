COUNTING_SORT_MAX = 1000


def counting_sort(data):
    # cheat in python
    # COUNTING_SORT_MAX = max(data) + 1
    count = [0] * COUNTING_SORT_MAX
    result = [0] * len(data)
    # k
    for value in data:
        count[value] += 1
    # n
    for i in range(1, COUNTING_SORT_MAX):
        count[i] += count[i - 1]
    # k
    for value in reversed(data):
        result[count[value] - 1] = value
        count[value] -= 1
    return result
