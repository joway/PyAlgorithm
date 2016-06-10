"""
桶排序假设输入数据服从均匀分布

O (n)
"""
from utils.utils import get_digits


def bucket_sort(data, size=10, sort_func=sorted, *args, **kwargs):
    base = get_digits(max(data))
    buckets = [[] for i in range(size)]
    for i in data:
        buckets[i // 10 ** (base - 1)].append(i)
    result = []
    for i in buckets:
        result.extend(sort_func(i, *args, **kwargs))
    return result
