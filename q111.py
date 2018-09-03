"""
Date: 2018/8/19
最小深度可以用BFS，遇到叶子节点就返回
但是DFS也可以，没超时？
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BFS(self, root):
        if not root:
            return 0

        stack = [root]
        depth = 1
        while len(stack) > 0:
            nums = len(stack)

            while nums > 0:
                node = stack.pop(0)
                nums -= 1
                if not node.left and not node.right:
                    return depth
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            depth += 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.BFS(root)

    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            left = self.minDepth2(root.left)
            right = self.minDepth2(root.right)
            if left > 0 and right > 0:
                return 1 + min(left, right)
            else:
                return 1 + left + right


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.right = TreeNode(0)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(0)
    root.right.right.right.right = TreeNode(0)

    s = Solution()
    print(s.minDepth2(root))