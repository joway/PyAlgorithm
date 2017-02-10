""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    Example:
        nums = [1,1,2]
        >>
        Your function should return length = 2, with the first two elements of
        nums being 1 and 2 respectively. It doesn't matter what you leave
        beyond the new length.
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)
                                                

if __name__ == '__main__':
    nums = [1,1,2]
    result = Solution().removeDuplicates(nums)
    print(nums)
    print(result)
