from nose.tools import assert_equal

from sorts.QuickSort import quick_sort
from tests.sort.base_sort import BaseSortTestCase


class QuickBaseSortTestCase(BaseSortTestCase):
    def setUp(self):
        super().setUp()
        self.length = 1000

    def test_quick_sort(self):
        self.assertFalse(self.is_sorted(self.reverse_data))
        self.loop(quick_sort, self.data)

    def test_quick_sort_random(self):
        self.assertFalse(self.is_sorted(self.reverse_data))
        self.loop(quick_sort, self.data, is_random=True)

    def test_quick_sort_worst(self):
        self.assertFalse(self.is_sorted(self.reverse_data))
        self.loop(quick_sort, self.reverse_data)

