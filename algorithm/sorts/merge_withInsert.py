from algorithm.sorts.insert_sort import insert_sort
from algorithm.sorts.merge_sort import merge_sort, merge


def merge_with_insert(data, log_n):
    if len(data) <= 1:
        return data
    # n**2 <= n * log_n
    if len(data) <= log_n:
        return insert_sort(data)
    cur = int(len(data) / 2)
    return merge(merge_sort(data[:cur]),
                 merge_sort(data[cur:]))
