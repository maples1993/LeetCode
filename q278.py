"""
Date: 2018/9/13
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    tt = [0, 0, 0, 0, 0, 0]
    if tt[version] == 1:
        return False
    else:
        return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left

print(Solution().firstBadVersion(6))