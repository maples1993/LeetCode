"""
Date: 2018/9/26
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dif = 0
        for i in range(len(s)):
            dif ^= ord(s[i])

        for i in range(len(t)):
            dif ^= ord(t[i])

        return chr(dif)


print(Solution().findTheDifference('abcd', 'abcde'))