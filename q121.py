"""
Date: 2018/8/21
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy = 0
        sell = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                profit = max(prices[sell] - prices[buy], profit)
                buy = sell = i
            if prices[i] > prices[sell]:
                sell = i
        return max(profit, prices[sell] - prices[buy])


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 9]
    print(s.maxProfit(prices))
