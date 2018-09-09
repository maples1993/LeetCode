"""
Date: 2018/9/8
建立  字符->位置  的映射表
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = [0] * 256
        map2 = [0] * 256
        for i in range(len(s)):
            if map1[ord(s[i])] != map2[ord(t[i])]:
                return False
            map1[ord(s[i])] = i + 1
            map2[ord(t[i])] = i + 1
        return True
