import random

from search.BinarySearch import binary_search
from sort.MergeSort import merge_sort
from tests.GeneralTestCase import GeneralTestCase


class SearchTest(GeneralTestCase):
    def setUp(self):
        super().setUp()
        self.length = 1000
        self.data = merge_sort(self.init_data())
        print(self.data)

    def init_data(self):
        data = []
        for i in range(0, self.length):
            data.append(int(random.random() * self.length))
        return data

    def loop(self, func, *args, **kwargs):
        count = 10
        for i in range(count):
            self.assertTrue(self.is_sorted(func(*args, **kwargs)))

    def is_sorted(self, data):
        for i in range(1, len(data)):
            if data[i - 1] > data[i]:
                return False
        return True

    def test_binary_search(self):
        value = self.data[500]
        cur = binary_search(value, self.data)
        self.assertEqual(cur, 500)