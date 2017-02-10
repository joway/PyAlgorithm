""" Summary
1. 对于递归类算法 , 首先要严格定义这个函数是做什么的, 参数和返回是什么
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/combination-sum-iii/
    Example:
        Example 1:
        Input: k = 3, n = 7
        Output:
        [[1,2,4]]

        Example 2:
            Input: k = 3, n = 9
        Output:
            [[1,2,6], [1,3,5], [2,3,4]]
    """

    def search(self, pre_nums, k, n):
        rets = []
        _start = max(pre_nums) + 1 if pre_nums else 1
        for i in range(_start, 10):
            _cur = pre_nums + [i]
            if k == 1 and i == n:
                rets += [_cur]
                break
            if k > 1 and i < n:
                rets += self.search(_cur, k - 1, n - i)
        return rets

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.search([], k, n)


if __name__ == '__main__':
    result = Solution().combinationSum3(3, 9)
    print(result)
