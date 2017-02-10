""" Summary

"""


class Solution(object):
    """
    Problem:

    Example:

    """

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        triangle = [[1]]
        for row in range(1, numRows):
            layer = [1]
            if row == 0:
                continue
            for col in range(1, row):
                layer.append(triangle[row - 1][col-1] + triangle[row - 1][col])
            layer.append(1)
            triangle.append(layer)
        return triangle


if __name__ == '__main__':
    numRows = 5
    result = Solution().generate(numRows)
    print(result)
