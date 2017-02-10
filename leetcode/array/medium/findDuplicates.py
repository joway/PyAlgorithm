""" Summary
只允许使用O(n)空间 且 element 属于 [1, len(nums)] ) 题目常用思路 :

令 nums[abs(element) - 1] *= -1
从而当某个元素值 < 0 的时候, 它的索引值(即另一个元素的element value ) 已经被遍历过了
又因为是取相反数, 所以在遍历变化过程中, 所有元素的值信息并不会丢失

Hint : 为了节约空间，可以考虑通过数学方式在限定空间里夸大数字隐含的信息量
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/find-all-duplicates-in-an-array/
    Example:
        Input:
        [4,3,2,7,8,2,3,1]

        Output:
        [2,3]
    """

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                ret.append(abs(nums[i]))
            nums[abs(nums[i]) - 1] *= -1
        return ret


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDuplicates(nums)
    print(result)
