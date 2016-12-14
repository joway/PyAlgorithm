"""
n * log n
"""
from datastructure.trees.binary_heap import BinaryHeap
from utils.exceptions import DataFormatException


def heap_sort(heap, is_max_heap=True):
    if isinstance(heap, list):
        heap = BinaryHeap(data=heap, is_max_heap=is_max_heap)
    if not isinstance(heap, BinaryHeap):
        raise DataFormatException
    result = []
    for i in range(heap.size - 1, -1, -1):
        result.append(heap.top())
        heap.swap(0, i)
        heap.del_last()
        heap.down_heapify(0)
    return result
