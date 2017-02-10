""" Summary
双指针法: 一个快指针，一个慢指针，遍历数组, 时间复杂度 O(n)

对于寻找子连续序列的题目, 可以采用滑动窗口的的思路, [left, right] 为一个窗口, 往后面移动
"""
import sys


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/minimum-size-subarray-sum/
    Example:
        INPUT : [2,3,1,2,4,3] , 7
        OUTPUT : [4, 3]
    """

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = sys.maxsize
        total = left = right = 0
        while right < len(nums):
            total += nums[right]
            while total >= s and left <= right:
                min_len = min(right - left + 1, min_len)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if min_len == sys.maxsize else min_len


if __name__ == '__main__':
    nums = [1,4,4]
    result = Solution().minSubArrayLen(4, nums)
    print(result)
