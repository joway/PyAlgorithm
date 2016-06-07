from sorts.InsertSort import insert_sort
from tests.sort.base_sort import BaseSortTestCase


class InsertBaseSortTestCase(BaseSortTestCase):
    def test_insert_sort(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(insert_sort, self.data)

    def test_insert_sort_worst(self):
        self.loop(insert_sort, self.reverse_data)
