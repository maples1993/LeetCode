"""
Date: 2018/9/8
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) != len(nums):
            return True
        else:
            return False