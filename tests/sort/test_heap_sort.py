from algorithm.sorts.heap_sort import heap_sort
from datastructure.trees.binary_heap import BinaryHeap
from tests.sort.base_sort import BaseSortTestCase


class HeapSortTestCase(BaseSortTestCase):
    def setUp(self):
        super().setUp()
        self.max_heap = BinaryHeap(self.data)
        self.min_heap = BinaryHeap(self.data, is_max_heap=False)

    def test_heap_sort_max(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(heap_sort, self.max_heap)
        self.assertTrue(self.is_sorted(heap_sort(self.max_heap)), True)

    def test_heap_sort_min(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(heap_sort, self.min_heap)
        self.assertTrue(self.is_sorted(heap_sort(self.min_heap)), True)

