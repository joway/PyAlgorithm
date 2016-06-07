# Binary Search Tree
class Node(object):
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.value)


class BSTree(object):
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, value):
        if isinstance(value, (list, tuple)):
            for i in value:
                self.insert(i)
            return True
        if self.root is None:
            self.root = Node(value)
            self.height += 1
            return True
        cur = self.root
        cur_height = 1
        while cur:
            cur_height += 1
            if value == cur.value:
                return False
            elif value < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(value)
                    cur.left.parent = cur
                    break
            elif value > cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(value)
                    cur.right.parent = cur
                    break
        if self.height < cur_height:
            self.height = cur_height
        return True

    # 前序遍历
    def pre_search(self, val, node=None):
        if not node:
            return None
        if node.value == val:
            return node
        result = self.pre_search(val, node.left)
        if result:
            return result
        return self.pre_search(val, node.right)

    # 中序遍历
    def in_search(self, val, node=None):
        if not node:
            return None
        result = self.in_search(val, node.left)
        if result:
            return result
        print(node)
        if node.value == val:
            return node
        return self.in_search(val, node.right)

    # 后序遍历
    def post_search(self, val, node=None):
        if not node:
            return None
        result = self.post_search(val, node.left)
        if result:
            return result
        result = self.post_search(val, node.right)
        if result:
            return result
        print(node)
        if node.value == val:
            return node

    def search(self, val, flag):
        if flag == 1:
            return self.pre_search(val, self.root)
        elif flag == 2:
            return self.in_search(val, self.root)
        elif flag == 3:
            return self.post_search(val, self.root)

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

    def delete(self, val):
        result = self.search(val, 1)
        if not result:
            return False
        if result.left is None and result.right is None:
            if result.parent.left == result:
                result.parent.left = None
            elif result.parent.right == result:
                result.parent.right = None
        elif result.left and not result.right:
            if result.parent.left == result:
                result.parent.left = result.left
            elif result.parent.right == result:
                result.parent.right = result.left
        elif result.right and not result.left:
            if result.parent.left == result:
                result.parent.left = result.right
            elif result.parent.right == result:
                result.parent.right = result.right
        elif result.left and result.right:
            if result.parent.left == result:
                cur = result
                max_val = self.maximum(result.left)
                result.parent.left = max_val
                self.delete(max_val)
                while cur:
                    result.left.right = result.right
            elif result.parent.right == result:
                result.parent.right = result.right

    def show(self):
        print(self.height)
        # space = '    '
        # cur = self.root
        # print(cur)
        # for i in range(1, self.height + 1):
        #     print(cur.left, cur.right)
        #     cur = cur
        # print(self.height)


'''
        3
    2        4
1    2.5    3.5    5
'''
tree = BSTree()
tree.insert([3, 2, 4, 1, 2.5, 3.5, 5])
print(tree.search(2.5, 1).parent)
# print(trees.searches(4, 1))
tree.show()
