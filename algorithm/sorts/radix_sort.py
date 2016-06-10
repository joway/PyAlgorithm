"""
O(k * n)
"""
import math


def radix_sort(data, radix=10):
    # bits = log n 时, 最佳
    bits = int(math.ceil(math.log(max(data), radix)))
    # box = [(value % 10 ** (i + 1) // 10 ** i, value) for value in data]
    result = data
    for i in range(0, bits):
        # 以第 i 位数字为基准,对 data 元素进行排序:
        box = [(value % radix ** (i + 1) // radix ** i, value) for value in result]
        # 计数排序:
        count = [0] * radix
        # k
        for v in box:
            count[v[0]] += 1
        # n
        for i in range(1, radix):
            count[i] += count[i - 1]
        # k
        for v in reversed(box):
            result[count[v[0]] - 1] = v[1]
            count[v[0]] -= 1
    return result
