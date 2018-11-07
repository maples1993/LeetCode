"""
Date: 2018/10/27
求根公式
"""
import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(0.5 * (math.sqrt(1 + 8 * n) - 1))

print(Solution().arrangeCoins(1804232485))