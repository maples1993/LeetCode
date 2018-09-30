"""
Date: 2018/9/20
"""
import string


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = -1
        for char in string.ascii_lowercase:
            l, r = s.find(char), s.rfind(char)

            if l != -1 and l == r:
                if ret == -1:
                    ret = l
                else:
                    ret = min(ret, l)
        return ret