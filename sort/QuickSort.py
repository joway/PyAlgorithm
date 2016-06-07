"""
在平均状况下，排序n个项目要Ο(n log n)次比较。在最坏状况下则需要Ο(n2)次比较，
但这种状况并不常见。事实上，快速排序通常明显比其他Ο(n log n)算法更快，
因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。
"""


def quick_sort(data):
    if len(data) <= 1:
        return data
    # 这里的循环方式采用了维基百科里的方式
    # 进行多少次递归取决于 数据本身的乱顺程度
    return quick_sort([x for x in data[1:] if x < data[0]]) + \
           [data[0]] + quick_sort([x for x in data[1:] if x >= data[0]])


