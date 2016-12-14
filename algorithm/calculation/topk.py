"""
优先级队列
"""


def top_k_order_by_value(ary: list, k):
    if len(ary) < k:
        return None
    result = ary[:k]
    for i in range(k, len(ary)):
        if ary[i] > min(result):
            result[result.index(min(result))] = ary[i]
    return result


def top_k_order_by_frequency(ary: list, k):
    pass


data = [1, 23, 4, 5, 6, 7, 12]
print(top_k_order_by_value(data, 3))
