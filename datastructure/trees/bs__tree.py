# Binary Search Tree
from datastructure.trees import binary_tree


class BSTree(binary_tree):
    def __init__(self, value):
        super().__init__(value)

    # def insert(self, value):
    #     if isinstance(value, (list, tuple)):
    #         for i in value:
    #             self.insert(i)
    #         return True
    #     if self.root is None:
    #         self.root = Node(value)
    #         self.height += 1
    #         return True
    #     cur = self.root
    #     cur_height = 1
    #     while cur:
    #         cur_height += 1
    #         if value == cur.value:
    #             return False
    #         elif value < cur.value:
    #             if cur.left:
    #                 cur = cur.left
    #             else:
    #                 cur.left = Node(value)
    #                 cur.left.parent = cur
    #                 break
    #         elif value > cur.value:
    #             if cur.right:
    #                 cur = cur.right
    #             else:
    #                 cur.right = Node(value)
    #                 cur.right.parent = cur
    #                 break
    #     if self.height < cur_height:
    #         self.height = cur_height
    #     return True


    def minimum(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def maximum(self, node):
        cur = node
        while cur.right:
            cur = cur.right
        return cur

    def successor(self):
        pass

    # def delete(self, val):
    #     result = self.search(val, 1)
    #     if not result:
    #         return False
    #     if result.left is None and result.right is None:
    #         if result.parent.left == result:
    #             result.parent.left = None
    #         elif result.parent.right == result:
    #             result.parent.right = None
    #     elif result.left and not result.right:
    #         if result.parent.left == result:
    #             result.parent.left = result.left
    #         elif result.parent.right == result:
    #             result.parent.right = result.left
    #     elif result.right and not result.left:
    #         if result.parent.left == result:
    #             result.parent.left = result.right
    #         elif result.parent.right == result:
    #             result.parent.right = result.right
    #     elif result.left and result.right:
    #         if result.parent.left == result:
    #             cur = result
    #             max_val = self.maximum(result.left)
    #             result.parent.left = max_val
    #             self.delete(max_val)
    #             while cur:
    #                 result.left.right = result.right
    #         elif result.parent.right == result:
    #             result.parent.right = result.right

'''
        3
    2        4
1    2.5    3.5    5
'''
# tree = BSTree()
# tree.insert([3, 2, 4, 1, 2.5, 3.5, 5])
# print(tree.search(2.5, 1).parent)
# print(trees.searches(4, 1))
# tree.show()
