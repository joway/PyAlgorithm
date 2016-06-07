"""
最好情况: n * log n
平均: n * log n
最坏 : n^2 (当数据是正序/逆序排列好时)
事实上，快速排序通常明显比其他Ο(n log n)算法更快，
因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。

解决快速排序的最坏情况方法:
1. 随机初始化打乱数据
2. 使用随机主元 (随机快速排序)
"""
import random

"""
当递归深度到达一定时候, python 会报错
python 默认递归最大深度为: 1000
可使用 sys.setrecursionlimit(1500) 修改默认值
"""


def quick_sort(data, is_random=False):
    # 这里的循环方式采用了维基百科里的方式
    # 进行多少次递归取决于 数据本身的乱顺程度
    if len(data) <= 1:
        return data
    if is_random:
        pivot = int(random.randint(0, len(data) - 1))
        data[0], data[pivot] = data[pivot], data[0]
    return quick_sort([x for x in data[1:] if x < data[0]]) \
           + [data[0]] + quick_sort([x for x in data[1:] if x >= data[0]])
