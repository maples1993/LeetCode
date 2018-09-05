"""
Date: 2018/9/5
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype:
        """
        res = []
        while n != 0:
            code = n % 2
            res.append(code)
            n //= 2
        return res[::-1]


print(Solution().convertToTitle(8))