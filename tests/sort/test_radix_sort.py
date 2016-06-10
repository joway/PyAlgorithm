from algorithm.sorts.radix_sort import radix_sort
from tests.sort.base_sort import BaseSortTestCase


class RadixSortTestCase(BaseSortTestCase):
    def test_radix_sort(self):
        self.loop(radix_sort, self.data)

    def test_radix_sort_binary_radix(self):
        self.loop(radix_sort, self.data, 2)
