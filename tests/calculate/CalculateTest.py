from calculate.Power import power, power_bad
from tests.GeneralTestCase import GeneralTestCase


class CalculateTest(GeneralTestCase):
    def setUp(self):
        super().setUp()
        self.num = 1000000

    def test_power(self):
        self.loop(power, 20, self.num)

    def test_power_bad(self):
        self.loop(power_bad, 20, self.num)
