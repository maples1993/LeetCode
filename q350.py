"""
Date: 2018/9/15
"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):     # nums2比较短
            nums1, nums2 = nums2, nums1

        ret = []
        num_dict = {}
        for x in nums2:
            num_dict[x] = num_dict.get(x, 0) + 1

        for x in nums1:
            if x in num_dict and num_dict[x] > 0:
                num_dict[x] -= 1
                ret.append(x)

        return ret

