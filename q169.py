"""
Date: 2018/9/6
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = None
        count = 0

        for x in nums:
            if count == 0:
                major = x
                count += 1
            elif x == major:
                count += 1
            else:
                count -= 1
        return major
