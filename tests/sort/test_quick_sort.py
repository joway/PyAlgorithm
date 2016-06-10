from algorithm.sorts.quick_sort import quick_sort
from tests.sort.base_sort import BaseSortTestCase


class QuickBaseSortTestCase(BaseSortTestCase):
    def test_quick_sort(self):
        self.loop(quick_sort, self.data)

    def test_quick_sort_random(self):
        self.loop(quick_sort, self.data, is_random=True)

    def test_quick_sort_worst(self):
        self.loop(quick_sort, self.reverse_data)

