"""
Date: 2018/8/15
如果直接翻转可能会遇到数值溢出的问题
因此可以只翻转一半
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x != 0 and x % 1 == 0:
            return False
        x_old = x
        x_new = 0
        while x_old > x_new:
            x_new = x_new * 10 + x_old % 10
            x_old = x_old // 10

        return x_old == x_new or x_old == x_new//10


if __name__ == '__main__':
    x = 10
    s = Solution()
    print(s.isPalindrome(x))