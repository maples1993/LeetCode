"""
Date: 2018/8/16
不用从数组中删除元素，可以只返回前几个
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)


if __name__ == '__main__':
    nums = [3, 2, 2, 3]

    s = Solution()
    print(s.removeElement(nums, 3))