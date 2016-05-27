from graph.Floyd import Floyd
from tests.GeneralTestCase import GeneralTestCase


class FloydTest(GeneralTestCase):
    def test_search(self):
        floyd = Floyd(10)
        floyd.show()
        floyd.show_sorted()
