from algorithm.sorts.heap_sort import heap_sort
from datastructure.trees.binary_heap import BinaryHeap
from tests.sort.base_sort import BaseSortTestCase


class HeapSortTestCase(BaseSortTestCase):
    def setUp(self):
        super().setUp()
        self.max_heap = BinaryHeap(self.data)
        self.min_heap = BinaryHeap(self.data, is_max_heap=False)

    def test_heap_sort_max(self):
        self.loop(heap_sort, self.max_heap, increasing=False)

    def test_heap_sort_min(self):
        self.loop(heap_sort, self.min_heap)

