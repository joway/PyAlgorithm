from datastructure.trees.binary_tree import BinaryTree
from tests.base_test_case import BaseTestCase


class BinaryTreeTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.length = 1000

    def test_binary_tree(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        tree = BinaryTree(data=data)
        # print('---')
        # tree.search_level(2)
        tree.show()
        # t = [1, 2, 3]
        # print(t[0:2])

