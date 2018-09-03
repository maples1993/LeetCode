"""
Date: 2018/8/15
要判断数值溢出
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = False
        if x < 0:
            x = abs(x)
            sign = True
        new_x = 0
        while x > 0:
            new_x = 10 * new_x + x % 10
            x = x // 10
        new_x &= 0xFFFFFFFF     # LeetCode加上这一行不通过
        if new_x <= 0x7FFFFFFF and sign:
            return -1 * new_x
        elif new_x <= 0x7FFFFFFF and not sign:
            return new_x
        else:
            return 0


if __name__ == '__main__':
    x = 1534236469
    s = Solution()
    print(s.reverse(x))