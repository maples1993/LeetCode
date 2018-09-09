"""
Date: 2018/9/6
记得考虑k>len的情况，要取模
"""


class Solution(object):
    def process(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - k % len(nums)
        self.process(nums, 0, k - 1)
        self.process(nums, k, len(nums) - 1)
        self.process(nums, 0, len(nums) - 1)
