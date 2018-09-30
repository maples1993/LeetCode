"""
Date: 2018/9/15
"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ret = num
        while abs(ret**2 - num) > 1e-9:
            ret = 0.5 * (ret + num / ret)
        return abs(ret - round(ret)) < 1e-9


print(Solution().isPerfectSquare(14))
