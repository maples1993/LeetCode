"""
Date: 2018/9/10
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        pivot = 0
        for i, x in enumerate(nums):
            if x == 0:
                count += 1
            else:
                nums[pivot] = x
                pivot += 1
            if pivot + count == len(nums):
                nums[pivot:] = [0] * count