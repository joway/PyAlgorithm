import math

from sorts.MergeSort import merge_sort
from sorts.MergeWithInsert import merge_with_insert
from tests.sort.SortTest import SortTest


class MergeSortTest(SortTest):
    def test_merge(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(merge_sort, self.data)

    def test_merge_worst(self):
        self.assertFalse(self.is_sorted(self.reverse_data))
        self.loop(merge_sort, self.reverse_data)

    def test_merge_with_insert(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(merge_with_insert, self.data, int(math.log(self.length, 2)))

    def test_merge_with_insert_worst(self):
        self.assertFalse(self.is_sorted(self.reverse_data))
        self.loop(merge_with_insert, self.reverse_data, int(math.log(self.length, 2)))