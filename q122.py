"""
Date: 2018/8/21
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[buy]:
                profit += prices[i] - prices[buy]
            buy = i
        return profit


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 4, 5]
    print(s.maxProfit(prices))