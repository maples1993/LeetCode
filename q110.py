"""
Date: 2018/8/19
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sub_balance(self, root):
        if not root:
            return 0

        left = self.sub_balance(root.left)
        right = self.sub_balance(root.right)
        if left is not False and right is not False:
            if abs(left - right) > 1:
                return False
            else:
                return 1 + max(left, right)
        else:
            return False

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.sub_balance(root) is not False:
            return True
        else:
            return False


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)

    s = Solution()
    print(s.isBalanced(root))

