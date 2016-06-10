"""
Parent(i) = floor((i-1)/2)，i 的父节点下标
Left(i) = 2i + 1，i 的左子节点下标
Right(i) = 2(i + 1)，i 的右子节点下标

"""

# 完全二叉树
import math

from utils.utils import max_with_none, min_with_none


class BinaryHeap(object):
    def __init__(self, data=None, is_max_heap=True):
        self.heap = []
        self.size = 0
        self.is_max_heap = is_max_heap
        self.init(data)

        # 创建最大堆

    def init(self, data):
        for i in data:
            self.insert(i)

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.up_heapify(self.size - 1)

    # 上浮调整
    def up_heapify(self, i):
        if not i or i == 0:
            return
        if (self.is_max_heap and self.parent(i) < self.value(i)) \
                or (not self.is_max_heap and self.parent(i) > self.value(i)):
            self.swap(i, (i - 1) // 2)
            self.up_heapify((i - 1) // 2)
        else:
            return

    # 下沉调整
    def down_heapify(self, i):
        if 2 * i + 1 > self.size - 1:
            return
        if self.is_max_heap:
            if self.value(i) >= max_with_none(self.left(i), self.right(i)):
                return
            if self.left(i) >= max_with_none(self.right(i), self.value(i)):
                target = 2 * i + 1
            else:
                target = 2 * (i + 1)
        else:
            if self.value(i) <= min_with_none(self.left(i), self.right(i)):
                return
            if self.left(i) <= min_with_none(self.right(i), self.value(i)):
                target = 2 * i + 1
            else:
                target = 2 * (i + 1)
        self.swap(i, target)
        self.down_heapify(target)

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def del_last(self):
        self.heap.pop()
        self.size -= 1

    def top(self):
        return self.heap[0]

    def left(self, pos):
        return self.value(2 * pos + 1)

    def right(self, pos):
        return self.value(2 * (pos + 1))

    def parent(self, pos):
        if not pos:
            return None
        return self.heap[(pos - 1) // 2]

    def value(self, pos):
        if pos < self.size:
            return self.heap[pos]
        return None

    def height(self, pos=None):
        """
        从 1 开始记数
        """
        if self.size == 0:
            return 0
        if pos is None:
            pos = self.size - 1
        return math.floor(math.log(pos + 1, 2)) + 1

    def __str__(self):
        result = ''
        partition = '   '
        for i in range(1, self.height() + 1):
            for j in range(2 ** (i - 1) - 1, 2 ** i - 1):
                try:
                    cell = str(self.heap[j])
                except IndexError:
                    break
                while len(cell) < 3:
                    cell = ' ' + cell + ' '
                result += partition * (self.height() - i) + cell
            result += '\n'
        return result
