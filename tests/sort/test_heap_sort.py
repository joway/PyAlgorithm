from algorithm.sorts.heap_sort import heap_sort
from datastructure.trees.binary_heap import BinaryHeap
from tests.sort.base_sort import BaseSortTestCase


class HeapSortTestCase(BaseSortTestCase):
    def test_heap_sort_max(self):
        self.assertFalse(self.is_sorted(self.data))
        heap = BinaryHeap(self.data)
        self.loop(heap_sort, heap)
        self.assertTrue(self.is_sorted(heap_sort(heap)), True)

    def test_heap_sort_min(self):
        self.assertFalse(self.is_sorted(self.data))
        heap = BinaryHeap(self.data, False)
        self.loop(heap_sort, heap)

