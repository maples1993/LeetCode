"""
Date: 2018/9/10
1. 异或找不匹配
2. 直接等差数列求和特性
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i, x in enumerate(nums):
            ret = ret ^ x ^ i
        return ret ^ len(nums)