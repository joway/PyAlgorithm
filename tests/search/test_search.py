from algorithm.searches.binary_search import binary_search
from algorithm.sorts.merge_sort import merge_sort
from tests.base_test_case import BaseTestCase


class SearchTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.unique_data = merge_sort(self.unique_data)
        self.data = merge_sort(self.data)

    def test_binary_search(self):
        print(self.unique_data[0], self.unique_data)
        self.assertEqual(binary_search(self.unique_data[0], self.unique_data), 0)
        self.assertEqual(binary_search(self.unique_data[len(self.unique_data) - 1], self.unique_data),
                         len(self.unique_data) - 1)
        self.assertEqual(binary_search(self.unique_data[len(self.unique_data) // 2], self.unique_data), len(self.unique_data) // 2)
        self.assertEqual(binary_search(-100000, self.data), -1)
