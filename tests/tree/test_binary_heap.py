from datastructure.trees.binary_heap import BinaryHeap
from tests.base_test_case import BaseTestCase


class BinaryHeapTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

    def test_binary_tree(self):
        data = [x for x in range(0, 15)]
        heap = BinaryHeap(data, False)
        print(heap)
        heap.del_last()
        print(heap)