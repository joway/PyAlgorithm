from algorithm.numberTheory.fibonacci import fibonacci_log_n
from tests.base_test_case import BaseTestCase


class SearchTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.num = 100

    def test_fibonacci_log_n(self):
        print(fibonacci_log_n(self.num))
