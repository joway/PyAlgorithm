from algorithm.sorts.bucket_sort import bucket_sort
from algorithm.sorts.heap_sort import heap_sort
from algorithm.sorts.insert_sort import insert_sort
from algorithm.sorts.merge_sort import merge_sort
from tests.sort.base_sort import BaseSortTestCase


class BucketSortTestCase(BaseSortTestCase):
    def test_bucket_sort_sorted(self):
        self.loop(bucket_sort, self.data, 10, sorted)

    def test_bucket_sort_heap_sort(self):
        self.loop(bucket_sort, self.data, 10, heap_sort, False)

    def test_bucket_sort_insert(self):
        self.loop(bucket_sort, self.data, 10, insert_sort)

    def test_bucket_sort_merge(self):
        self.loop(bucket_sort, self.data, 10, merge_sort)
