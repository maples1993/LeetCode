"""
Date: 2018/8/18
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 2]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
