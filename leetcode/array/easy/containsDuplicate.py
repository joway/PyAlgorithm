""" Summary

"""


class Solution(object):
    """
    Problem:

    Example:

    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return nums != [] and len(nums) != len(set(nums))


if __name__ == '__main__':
    nums = []
    result = Solution().containsDuplicate(nums)
    print(result)
