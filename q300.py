"""
Date: 2018/9/19
"""


class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = x
            size = max(left + 1, size)
        return size

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0] * len(nums)
        max_len = 0
        for i, x in enumerate(nums):
            count[i] = 1

            for j in range(i):
                if nums[j] < nums[i] and count[j] + 1 > count[i]:
                    count[i] = count[j] + 1
            max_len = max(max_len, count[i])
        return max_len


print(Solution().lengthOfLIS([2, 7, 1, 5, 6, 4, 3, 8, 9]))