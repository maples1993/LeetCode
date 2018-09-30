"""
Date: 2018/9/26
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        while n - 9 * 10 ** step * (step + 1) > 0:
            n -= 9 * 10 ** step * (step + 1)
            step += 1

        pre_num = 10 ** step + n // (step + 1) - 1
        n -= n // (step + 1) * (step + 1)
        if n != 0:
            pre_num += 1
            pre_num //= 10 ** (step + 1 - n)

        return pre_num % 10


print(Solution().findNthDigit(100))