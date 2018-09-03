"""
Date: 2018/8/19
判断左右子树是否一样，转化为递归
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) \
                       and self.isSameTree(p.right, q.right)
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)

    s = Solution()
    print(s.isSameTree(root1, root2))