import math
import random

from sort.InsertSort import insert_sort
from sort.MergeSort import merge_sort
from sort.MergeWithInsert import merge_with_insert
from tests.GeneralTestCase import GeneralTestCase


class SortTest(GeneralTestCase):
    def setUp(self):
        super().setUp()
        self.length = 1000
        self.data = self.init_data()
        self.reverse_data = self.get_reverse_data()

    def init_data(self):
        data = []
        for i in range(0, self.length):
            data.append(int(random.random() * self.length))
        return data

    def get_reverse_data(self):
        return merge_sort(self.data)[::-1]

    def loop(self, func, *args, **kwargs):
        count = 10
        for i in range(count):
            self.assertTrue(self.is_sorted(func(*args, **kwargs)))

    def is_sorted(self, data):
        for i in range(1, len(data)):
            if data[i - 1] > data[i]:
                return False
        return True

    def test_insert_sort(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(insert_sort, self.data)

    def test_insert_sort_worst(self):
        self.loop(insert_sort, self.reverse_data)

    def test_merge(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(merge_sort, self.data)

    def test_merge_worst(self):
        self.assertFalse(self.is_sorted(self.reverse_data))
        self.loop(merge_sort, self.reverse_data)

    def test_merge_with_insert(self):
        self.assertFalse(self.is_sorted(self.data))
        self.loop(merge_with_insert, self.data, int(math.log(self.length, 2)))

    def test_merge_with_insert_worst(self):
        self.assertFalse(self.is_sorted(self.reverse_data))
        self.loop(merge_with_insert, self.reverse_data, int(math.log(self.length, 2)))
