from algorithm.sorts.radix_sort import radix_sort
from tests.sort.base_sort import BaseSortTestCase


class RadixSortTestCase(BaseSortTestCase):
    def test_radix_sort(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(radix_sort, self.data)
        self.assertTrue(self.is_sorted(radix_sort(self.data)))

    def test_radix_sort_binary_radix(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(radix_sort, self.data, 2)
        self.assertTrue(self.is_sorted(radix_sort(self.data)))
