""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/combination-sum/
    Example:
        given candidate set [2, 3, 6, 7] and target 7,
        A solution set is:
        [
          [7],
          [2, 2, 3]
        ]
    """

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        rets = []
        for i in candidates:
            if i > target:
                break
            elif i == target:
                rets.append([i])
            else:
                rets += ([sorted([i] + x) for x in self.combinationSum(candidates, target - i)])
        result = []
        for r in rets:
            if r not in result:
                result.append(r)

        return result


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    result = Solution().combinationSum(candidates, 7)
    print(result)
