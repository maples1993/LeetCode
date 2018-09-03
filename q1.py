"""
Date: 2018/8/15
解法1：暴力法for循环，时间复杂度O(n^2)，空间复杂度O(1)
解法2：使用Hash表，时间复杂度O(n)，空间复杂度O(n)
每次插入时检查是否存在相对应的元素，充分利用Hash表查找复杂度为O(1)的特性
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return None

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_dict:
                return [num_dict[comp], i]
            num_dict[num] = i
        return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]

    solution = Solution()
    print(solution.twoSum2(nums, 22))