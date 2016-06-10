from tests.base_test_case import BaseTestCase


class BaseSortTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.reverse_data = self.get_reverse_data()
        self.assertFalse(self.is_sorted(self.data))
        self.LOOP = 10

    def loop(self, func, *args, **kwargs):
        for i in range(self.LOOP):
            self.assert_sorted(func(*args), **kwargs)
