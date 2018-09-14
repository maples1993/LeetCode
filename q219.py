"""
Date: 2018/9/9
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_dict = {}
        for i, x in enumerate(nums):
            if x in num_dict and i - num_dict[x] <= k:
                return True
            num_dict[x] = i
        return False
