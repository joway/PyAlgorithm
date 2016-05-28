from numberTheory.Fibonacci import fibonacci_log_n
from tests.GeneralTestCase import GeneralTestCase


class SearchTest(GeneralTestCase):
    def setUp(self):
        super().setUp()
        self.num = 100

    def test_fibonacci_log_n(self):
        print(fibonacci_log_n(self.num))
