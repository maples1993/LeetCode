"""
Date: 2018/8/17
用DP思想2行代码就解决了：
如果curSum+x还比x小，那就说明当前curSum<0，可以重新选择起点了
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_max = nums[0]
        max_sum = [tmp_max]
        for i in range(1, len(nums)):
            if tmp_max < 0 and nums[i] > tmp_max:   # 清空结果
                tmp_max = nums[i]
            else:
                if nums[i] < 0:
                    max_sum.append(tmp_max)
                tmp_max += nums[i]
            if tmp_max > max_sum[-1]:
                max_sum[-1] = tmp_max
        return max(max_sum)

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        cur_sum = max_sum = nums[0]
        for x in nums[1:]:
            cur_sum = max(x, cur_sum + x)
            max_sum = max(cur_sum, max_sum)
        return max_sum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    s = Solution()
    print(s.maxSubArray2(nums))


