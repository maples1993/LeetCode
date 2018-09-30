"""
Date: 2018/9/26
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def process(self, root, type):
        if not root:
            return 0

        if not root.left and not root.right and type == 0:
            return root.val

        return self.process(root.left, 0) + self.process(root.right, 1)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.process(root.left, 0) + self.process(root.right, 1)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().sumOfLeftLeaves(root))