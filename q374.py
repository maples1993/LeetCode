"""
Date: 2018/9/20
"""


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 1:
                left = mid + 1
            elif res == -1:
                right = mid - 1
            else:
                return mid


print(Solution().guessNumber(10))