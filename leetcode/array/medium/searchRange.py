""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/search-for-a-range/
    Example:
        Given [5, 7, 7, 8, 8, 10] and target value 8,
        return [3, 4]
    """

    def binary_search(self, val, sorted_data):
        length = len(sorted_data)
        # [start, stop]
        start = 0
        stop = length - 1
        while start <= stop:
            mid = (stop + start) // 2
            if sorted_data[mid] < val:
                start = mid + 1
            elif sorted_data[mid] > val:
                stop = mid - 1
            else:
                return mid
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = self.binary_search(target, nums)
        if pos == -1:
            return [-1, -1]
        start = pos
        end = pos
        left = 1
        right = 1
        while left or right:
            if left and pos - left >= 0 and nums[pos - left] == target:
                start = pos - left
                left += 1
            else:
                left = 0
            if right and pos + right < len(nums) and nums[pos + right] == target:
                end = pos + right
                right += 1
            else:
                right = 0
        return [start, end]


if __name__ == '__main__':
    # nums = [5, 7, 7, 8, 8, 10]
    nums = [2, 2]
    result = Solution().searchRange(nums, 3)
    print(result)
