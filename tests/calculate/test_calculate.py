from algorithm.calculation.power import power, power_bad
from tests.base_test_case import BaseTestCase


class CalculateTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.num = 1000000

    def test_power(self):
        self.loop(power, 20, self.num)

    def test_power_bad(self):
        self.loop(power_bad, 20, self.num)
