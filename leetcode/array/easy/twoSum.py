""" Summary

"""


class Solution(object):
    """
    Problem:
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution.
    Example:
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        O(n^2)
        """
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y and nums[x] + nums[y] == target:
                    return [x, y]

    def twoSumBest(self, nums, target):
        """
        O(n)
        """
        if len(nums) <= 1:
            return False
        # hashmap : key = target - array_value, value = array_index
        # 解题思路相当于顺序寻找另一半
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
