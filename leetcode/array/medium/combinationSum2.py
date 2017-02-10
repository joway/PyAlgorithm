""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/combination-sum-ii/
    Example:
        given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
        A solution set is:
        [
          [1, 7],
          [1, 2, 5],
          [2, 6],
          [1, 1, 6]
        ]
    """

    def combinationSum2(self, candidates, target, init=True):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if init:
            candidates.sort()
        rets = []
        for i in candidates:
            if i > target:
                break
            elif i == target:
                rets.append([i])
            else:
                _temp = list(candidates)
                _temp.remove(i)
                rets += ([sorted([i] + x) for x in self.combinationSum2(_temp, target - i, False)])
        result = []
        for r in rets:
            if r not in result:
                result.append(r)

        return result


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = Solution().combinationSum2(candidates, target)
    print(result)
