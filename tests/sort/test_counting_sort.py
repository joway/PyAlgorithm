from algorithm.sorts.counting_sort import counting_sort
from tests.sort.base_sort import BaseSortTestCase


class CountingSortTestCase(BaseSortTestCase):
    def setUp(self):
        super().setUp()

    def test_count_sort_max(self):
        self.loop(counting_sort, self.data)
