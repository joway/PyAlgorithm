""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/max-consecutive-ones/
    Example:
        Input: [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.
    """

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
                if count > result:
                    result = count
            else:
                count = 0
        return result


if __name__ == '__main__':
    nums = [0, 1]
    result = Solution().findMaxConsecutiveOnes(nums)
    print(result)
