"""
Date: 2018/8/19
也可以用队列进行BFS，不过得左右两个分支都要入队
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subSym(self, left_node, right_node):
        if left_node and right_node:
            return left_node.val == right_node.val \
                   and self.subSym(left_node.left, right_node.right) \
                   and self.subSym(left_node.right, right_node.left)
        elif not left_node and not right_node:
            return True
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.subSym(root.left, root.right)
        else:
            return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    # root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)

    s = Solution()
    print(s.isSymmetric(root))