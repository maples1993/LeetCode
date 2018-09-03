"""
Date: 2018/8/19
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balance_tree(self, nums, left, right):
        root = None
        if right - left <= 1:
            for i in range(right, left-1, -1):
                if not root:
                    root = TreeNode(nums[i])
                else:
                    root.left = TreeNode(nums[i])
        else:
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = self.balance_tree(nums, left, mid-1)
            root.right = self.balance_tree(nums, mid+1, right)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            return self.balance_tree(nums, 0, len(nums)-1)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]

    s = Solution()
    print(s.sortedArrayToBST(nums))