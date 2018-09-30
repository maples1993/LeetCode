"""
Date: 2018/9/15
"""


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        bits = 1
        while num & 1 == 0:
            num >>= 1
            bits += 1
        num >>= 1

        return num == 0 and bits % 2 == 1
