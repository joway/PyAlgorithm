""" Summary

"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/plus-one/
    Example:
        input: [1,2,9,9]
        output: [1,3,0,0]
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        remainder = 0
        for i in range(len(digits) - 1 , -1 , -1):
            r = digits[i] + carry + remainder
            if r >= 10:
                carry = 1
                remainder = r % 10
            else:
                carry = 0
                remainder = 0
            digits[i] = r % 10
        if carry and digits[0] == 0:
            digits = [1] + digits

        return digits                         


if __name__ == '__main__':
    digits = [9]
    result = Solution().plusOne(digits)
    print(result)
