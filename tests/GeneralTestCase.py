import unittest


class GeneralTestCase(unittest.TestCase):
    def setUp(self):
        print('-----------------------')
        print('Begin', self.__class__)

    def tearDown(self):
        print('End', self.__class__)
        print('-----------------------')

    def loop(self, func, *args, **kwargs):
        count = 10
        for i in range(count):
            func(*args, **kwargs)

    def is_sorted(self, data):
        for i in range(1, len(data)):
            if data[i - 1] > data[i]:
                return False
        return True
