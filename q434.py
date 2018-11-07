"""
Date: 2018/10/22
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        flag = False
        count = 0
        for c in s:
            if c == ' ' and flag:
                count += 1
                flag = False
            if c != ' ' and not flag:
                flag = True
        if s[-1] != ' ':
            count += 1
        return count

print(Solution().countSegments(' 3'))