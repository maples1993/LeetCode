"""
Date: 2018/9/14
先手玩家只需要让剩下的石头为4的倍数即可
"""


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0