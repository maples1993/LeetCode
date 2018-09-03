"""
Date: 2018/8/18
从后往前合并可以减少元素移动次数
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        while i2 < n:
            while nums2[i2] > nums1[i1] and i1 < m:
                i1 += 1
            for k in range(m-1, i1-1, -1):
                nums1[k+1] = nums1[k]
            nums1[i1] = nums2[i2]
            i2 += 1
            m += 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0, 0, 0]
    nums2 = [0, 2, 4, 5, 6]

    s = Solution()
    s.merge(nums1, 3, nums2, 5)
    print(nums1)