"""
Date: 2018/9/6
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        bit = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            res += 26 ** bit * (ord(s[i]) - ord('A') + 1)
            bit += 1
        return res