import unittest


class GeneralTestCase(unittest.TestCase):
    def setUp(self):
        print('-----------------------')
        print('Begin', self.__class__)

    def tearDown(self):
        print('End', self.__class__)
        print('-----------------------')

