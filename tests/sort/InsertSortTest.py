from sorts.InsertSort import insert_sort
from tests.sort.SortTest import SortTest


class InsertSortTest(SortTest):
    def test_insert_sort(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(insert_sort, self.data)

    def test_insert_sort_worst(self):
        self.loop(insert_sort, self.reverse_data)
