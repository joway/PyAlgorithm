""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
    Example:
        Input:
            [4,3,2,7,8,2,3,1]

        Output:
            [5,6]
    """
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 这个算法会超时
        ret = []
        ret_len = len(nums) - len(set(nums)) 
        for i in range(1, len(nums)+ 1):
            if i not in nums:
                ret.append(i)
            if len(ret) == ret_len:
                break
        return ret
        
    def findDisappearedNumbersBest(self, nums):
        for i in range(len(nums)):
            # index = 当前元素值 - 1
            index = abs(nums[i]) - 1
            # nums[index] 取负数, 这样所有存在的 ( 元素值 - 1 ) 的坐标的数都会是负数了
            nums[index] = -abs(nums[index])
        # 仍旧值 >0 的数, 说明没有一个元素等于其坐标 + 1, 即不存在的值
        return [x + 1 for x in range(len(nums)) if nums[x] > 0]


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    result = Solution().findDisappearedNumbers(nums)
    print(result)
