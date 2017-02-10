""" Summary
zip: 接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/pascals-triangle-ii/
    Example:
        given k = 3,
        Return [1,3,3,1].
    """
    def __init__(self):
        self.cache = {}

    def getItem(self, row, col):
        if col == 0 or col == row:
            return 1
        key = '%s-%s' % (row, col)
        cached = self.cache.get(key, None)
        if cached:
            return self.cache.get(key, None)

        self.cache[key] = self.getItem(row - 1, col - 1) + self.getItem(row - 1, col)
        return self.cache[key]

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return [self.getItem(rowIndex, col) for col in range(rowIndex + 1)]

    def getRowBest(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [t[0] + t[1] for t in zip([0] + row, row + [0])]
        return row


if __name__ == '__main__':
    result = Solution().getRow(100)
    # result = Solution().getRowBest(100)
    print(result)
