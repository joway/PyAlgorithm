""" Summary
    
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/remove-element/
    Example:
        Given input array nums = [3,2,2,3], val = 3

        Your function should return length = 2, with the first two elements of
        nums being 2.
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums) 



if __name__ == '__main__':
    result = Solution().removeElement()
    print(result)
