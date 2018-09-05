"""
Date: 2018/9/5
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return []

        i1 = 0
        i2 = len(numbers) - 1
        while i1 < i2:
            if numbers[i1] + numbers[i2] > target:
                i2 -= 1
            elif numbers[i1] + numbers[i2] < target:
                i1 += 1
            else:
                return [i1 + 1, i2 + 1]

        return []
