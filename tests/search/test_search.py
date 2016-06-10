from algorithm.searches.binary_search import binary_search
from algorithm.sorts.merge_sort import merge_sort
from tests.base_test_case import BaseTestCase


class SearchTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.data = merge_sort(self.init_data())

    def test_binary_search(self):
        value = self.data[len(self.data) // 2]
        cur = binary_search(value, self.data)
        self.assertEqual(cur, len(self.data) // 2)
