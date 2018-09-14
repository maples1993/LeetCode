"""
Date: 2018/9/13
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = []
        self.path = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            self.path.append(root.val)
        else:
            return []

        if not root.left and not root.right:
            self.res.append('->'.join([str(x) for x in self.path]))

        if root.left:
            self.binaryTreePaths(root.left)
        if root.right:
            self.binaryTreePaths(root.right)
        self.path.pop(-1)
        return self.res
