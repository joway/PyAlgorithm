""" Summary
sorted 速度要比max慢得多, 优选 max 函数
set() 可以去重
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/third-maximum-number/
    Example:
        Input: [3, 2, 1]

        Output: 1
        Explanation: The third maximum is 1.
    """

    def thirdMaxBest(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            return sorted(nums)[len(nums) - 3]


if __name__ == '__main__':
    nums = [3, 2, 1]
    result = Solution().thirdMax(nums)
