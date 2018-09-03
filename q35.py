"""
Date: 2018/8/17
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums and target <= nums[0]:
            return 0
        elif nums and target > nums[-1]:
            return len(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        return left


if __name__ == '__main__':
    nums = [1, 1, 3, 4, 5, 5, 5, 5]

    s = Solution()
    print(s.searchInsert(nums, 1))