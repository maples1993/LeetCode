"""
Date: 2018/9/8
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = {}
        while n != 1:
            ret = 0
            while n:
                ret += (n % 10) ** 2
                n //= 10
            if ret not in history:
                history[ret] = 1
            else:
                return False
            n = ret
        return True
