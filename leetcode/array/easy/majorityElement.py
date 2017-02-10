""" Summary
由于出现次数要 > 1/2 , 所以可以一个数用来抵消之前主要数的权重，最后最主要的数权重(count)必然>=1
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/majority-element/
    Example:
    """

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = len(nums) // 2 + 1
        dic = {}
        if len(nums) == 1:
            return nums[0]
        for n in nums:
            if str(n) in dic.keys():
                dic[str(n)] += 1
                if dic[str(n)] >= major:
                    return n
            else:
                dic[str(n)] = 1

    def majorityElementBest(self, nums):
        major = nums[0]
        count = 1
        for n in nums[1:]:
            if count == 0:
                count += 1
                major = n
            elif major == n:
                count += 1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 3, 3]
    # result = Solution().majorityElement(nums)
    result = Solution().majorityElementBest(nums)
    print(result)
