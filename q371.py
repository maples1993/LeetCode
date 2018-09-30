"""
Date: 2018/9/20
"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # a denotes sum, b denotes carry
        while b:
            a, b = a ^ b, (a & b) << 1

            a &= 0xFFFFFFFF
            b &= 0xFFFFFFFF

            if a > 0x7FFFFFFF:
                a ^= 0xFFFFFFFF
                a = ~a
        return a
