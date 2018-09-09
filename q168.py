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
            code = n % 26
            if code == 0:
                res.append(chr(26 - 1 + ord('A')))
                n /= 26
                n -= 1
            else:
                res.append(chr(code - 1 + ord('A')))
                n //= 26
        return ''.join(res[::-1])


print(Solution().convertToTitle(703))