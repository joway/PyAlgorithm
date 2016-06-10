import math

from datastructure.trees.tree import Tree

# 二叉树
from utils.exceptions import DataFormatException


class BinaryTree(Tree):
    def __init__(self, value=None, parent=None, left=None, right=None, data=None):
        super().__init__(value)
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
        if data:
            self.init(data)

    def init(self, data):
        if not data:
            return None
        self.value = data[0]
        for i in range(1, math.floor(math.log(len(data), 2)) + 1):
            cur_level_data = data[2 ** i - 1: 2 ** (i + 1) if 2 ** (i + 1) <= len(data) else len(data)]
            cur = 0
            try:
                for item in self.search_level(i - 1):
                    item.insert(cur_level_data[cur])
                    item.insert(cur_level_data[cur + 1])
                    cur += 2
            except IndexError:
                pass

    def insert(self, child, is_right=None):
        if self.left and self.right:
            return None
        if not isinstance(child, BinaryTree):
            try:
                child = BinaryTree(value=child)
            except TypeError:
                raise DataFormatException
        child.parent = self
        if is_right is None:
            # auto select
            if not self.left:
                self.left = child
            else:
                self.right = child
        elif is_right is True:
            self.right = child
        else:
            self.left = child
        child.height = self.height + 1
        return child

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

    def search(self, val):
        pass

    def search_level(self, level):
        # 广搜
        stack = [self]
        result = []
        while stack:
            cur = stack.pop(0)
            if cur.height == level:
                result.append(cur)
            elif cur.height > level:
                break
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result

    def status(self):
        pass

    def show(self, depth=0):
        # 中序遍历
        ret = ""
        # Print right branch
        if self.right:
            ret += self.right.show(depth + 1)
        # Print own value
        ret += "\n" + ("   " * depth) + str(self)
        # Print left branch
        if self.left:
            ret += self.left.show(depth + 1)
        if depth == 0:
            print(ret)
        return ret

    def value(self):
        return self.value

    def left(self):
        return self.left

    def right(self):
        return self.right

    def __str__(self, depth=0):
        return str(self.value)
