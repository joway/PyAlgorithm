from algorithm.sorts.insert_sort import insert_sort
from tests.sort.base_sort import BaseSortTestCase


class InsertBaseSortTestCase(BaseSortTestCase):
    def test_insert_sort(self):
        self.loop(insert_sort, self.data)

    def test_insert_sort_worst(self):
        self.loop(insert_sort, self.reverse_data)
