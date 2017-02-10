""" Summary
    在遍历价格数组时，根据这个动态更新的最低价和当前的价格可以算出当前卖股票最大能赚多少钱。
"""


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Example:
        Input: [7, 1, 5, 3, 6, 4]
        Output: 5
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return profit
        min_so_far = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_so_far)
            min_so_far = min(prices[i], min_so_far)
        return profit

                                                


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    result = Solution().maxProfit(prices)
    print(result)
