class ListNode(object):
    def __init__(self, val, pre=None, post=None):
        self.val = val
        self.pre = pre
        self.post = post

    def __str__(self):
        return str(self.val)

    def last(self):
        _last = self
        while _last.post:
            _last = _last.post
        return _last

    def is_last(self):
        return self.post is None

    def is_first(self):
        return self.pre is None

    def append(self, node):
        if self.post:
            self.post.pre = node
        self.post = node
        node.pre = self

    def insert(self, node):
        if self.pre:
            self.pre.post = node
        self.pre = node
        node.post = self

    def display(self):
        ret = '%s ' % self.val
        _pos = self.post
        while _pos:
            ret += ' --> %s' % _pos.val
            _pos = _pos.post

        print(ret)


if __name__ == '__main__':
    nodes = ListNode(1)
    nodes.append(ListNode(2))
    nodes.append(ListNode(3))
    nodes.append(ListNode(4))
    nodes.display()
