import random
import time
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        print('-----------------------')
        print('Begin', self.__class__)
        self.begin_at = time.time()
        self.MAX = 100
        self.LOOP = 1
        self.length = 100
        self.data = self.init_data()
        self.unique_data = list(set(self.data))

    def tearDown(self):
        print("Used time : %s s" % str((time.time() - self.begin_at))[:8])
        print('End', self.__class__)
        print('-----------------------')

    def loop(self, func, *args, **kwargs):
        for i in range(self.LOOP):
            kwargs.get('assert_func', print)(func(*args), kwargs.get('assert_data', []))

    def is_sorted(self, data, increasing=True, *args, **kwargs):
        for i in range(1, len(data)):
            if increasing:
                if data[i - 1] > data[i]:
                    return False
            else:
                if data[i - 1] < data[i]:
                    return False
        return True

    def init_data(self):
        data = []
        for i in range(0, self.length):
            data.append(int(random.random() * self.length))
        return data

    def get_reverse_data(self):
        return sorted(self.data)[::-1]

    def assert_sorted(self, data, *args, **kwargs):
        assert self.is_sorted(data, *args, **kwargs)

    def assert_equal(self, result, expect, *args):
        assert result == expect
