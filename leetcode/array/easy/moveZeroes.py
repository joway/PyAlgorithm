""" Summary
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/move-zeroes/
    Example:
        given nums = [0, 1, 0, 3, 12],
        after calling your function, nums should be [1, 3, 12, 0, 0]

    """

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur = 0
        non_zero = len(nums) - 1
        while cur < non_zero:
            if nums[cur] == 0:
                for i in range(cur + 1, non_zero + 1):
                    nums[i - 1] = nums[i]
                nums[non_zero] = 0
                non_zero -= 1
            else:
                cur += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    result = Solution().moveZeroes(nums)
    print(nums)
