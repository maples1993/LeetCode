"""
Date: 2018/9/14
不要每次都加，会有很多重复计算，用空间换时间
"""


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_index = [0] * len(nums)
        cur_sum = 0
        for i, x in enumerate(nums):
            cur_sum += x
            self.sum_index[i] = cur_sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or j >= len(self.sum_index):
            return None
        if i == 0:
            return self.sum_index[j]
        else:
            return self.sum_index[j] - self.sum_index[i-1]
