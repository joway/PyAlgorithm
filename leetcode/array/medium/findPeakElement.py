""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/find-peak-element/
    Example:
        For example, in array [1, 2, 3, 1], 3 is a peak element
        and your function should return the index number 2.
    """

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                index = i
        return index


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = Solution().findPeakElement(nums)
    print(result)
