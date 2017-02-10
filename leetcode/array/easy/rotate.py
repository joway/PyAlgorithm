""" Summary
- 注意 , k 是可能 > len(nums) 的
- nums[:] = [x,x,x , ... ]  能够进行引用替换
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/rotate-array/
    Example:
        n = 7 and k = 3
        the array [1,2,3,4,5,6,7] is rotated
        to [5,6,7,1,2,3,4].
    """
    def rotate(self, nums, k):
        k %= len(nums) 
        left = nums[len(nums)-k:]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = left[i]

    def rotateBest(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]




if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 10
    result = Solution().rotate(nums, 3)
    print(nums)

