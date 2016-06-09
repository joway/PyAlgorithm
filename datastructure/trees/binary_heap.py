"""
Parent(i) = floor((i-1)/2)，i 的父节点下标
Left(i) = 2i + 1，i 的左子节点下标
Right(i) = 2(i + 1)，i 的右子节点下标

"""

# 完全二叉树
import math


class BinaryHeap(object):
    def __init__(self, data=None):
        self.heap = []
        self.size = 0
        self.init(data)

    # 创建最大堆
    def init(self, data):
        for i in data:
            self.insert(i)

    def insert(self, value):
        self.heap.append(value)
        self.max_up_heapify(self.size)
        self.size += 1

    # 最大堆 上浮调整
    def max_up_heapify(self, i):
        if not i:
            return
        if self.parent(i) < self.value(i):
            self.swap(i, (i - 1) // 2)
            self.max_up_heapify((i - 1) // 2)
        else:
            return

    # 最大堆 下沉调整
    def max_down_heapify(self, i):
        if self.value(i) >= max(self.left(i), self.right(i)):
            return
        if self.value(i) < self.left(i):
            target = 2 * i + 1
        else:
            self.value(i) < self.right(i)
            target = 2 * (i + 1)
        self.swap(i, target)
        self.max_down_heapify(target)

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def left(self, pos):
        return self.heap[2 * pos + 1]

    def right(self, pos):
        return self.heap[2 * (pos + 1)]

    def parent(self, pos):
        if not pos:
            return None
        return self.heap[(pos - 1) // 2]

    def value(self, pos):
        return self.heap[pos]

    def height(self, pos=None):
        """
        从 1 开始记数
        """
        if pos is None:
            pos = self.size - 1
        return math.floor(math.log(pos + 1, 2)) + 1

    def __str__(self):
        result = ''
        partition = '    '
        for i in range(1, self.height() + 1):
            for j in range(2 ** (i - 1) - 1, 2 ** i - 1):
                try:
                    cell = str(self.heap[j])
                except IndexError:
                    break
                while len(cell) < 3:
                    cell = ' ' + cell
                result += partition * (self.height() - i) + cell
            result += '\n'
        return result
