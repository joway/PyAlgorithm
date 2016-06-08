import random

from sorts.MergeSort import merge_sort
from tests.base_test_case import BaseTestCase


class BaseSortTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.length = 1000000000
        self.data = self.init_data()
        self.reverse_data = self.get_reverse_data()

    def init_data(self):
        data = []
        for i in range(0, self.length):
            data.append(int(random.random() * self.length))
        return data

    def get_reverse_data(self):
        return merge_sort(self.data)[::-1]
