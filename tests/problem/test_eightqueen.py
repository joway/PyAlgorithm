from algorithm.problem import eightqueen
from tests.base_test_case import BaseTestCase


class EightQueenTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

    def test_eight_queen(self):
        self.loop(eightqueen, [1, 2, 4])
