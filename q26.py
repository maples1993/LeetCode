"""
Date: 2018/8/16
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i+1 < len(nums):
                if nums[i+1] == nums[i]:
                    nums.pop(i+1)
                else:
                    i += 1
            else:
                i += 1

        return len(nums)


if __name__ == '__main__':
    nums = [0,0]

    s = Solution()
    print(s.removeDuplicates(nums))