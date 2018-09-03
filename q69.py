"""
Date: 2018/8/18
解法1：牛顿法
解法2：二分法
"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        p = x
        while p * p - x >= 1:
            p = 0.5 * (p + x / p)
        return int(p)

    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None

        left = 0
        right = x
        while True:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                if (mid + 1) ** 2 > x:
                    return mid
                left = mid + 1


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt2(3))
