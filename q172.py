"""
Date: 2018/9/6
连续两个5的倍数之间肯定有2，所以只要统计5的个数就可以了
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            n //= 5
            res += n
        return res

print(Solution().trailingZeroes(105))