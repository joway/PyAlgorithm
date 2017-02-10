""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/contains-duplicate-ii/
    Example:
        INPUT : [1,2,3,4,1,5], 4
        OUTPUT : 0,4, True
    """
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cache = {}
        for i in range(len(nums)):
            if nums[i] in cache and i - cache.get(nums[i]) <= k:
                return True
            cache[nums[i]] = i
        return False





if __name__ == '__main__':
    nums = [1,2,3,4,1,5]
    k = 4
    result = Solution().containsNearbyDuplicate(nums, k)
    print(result)
