"""
Date: 2018/8/19
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root:
            stack = [root]
            nums = 1
            while len(stack) > 0:
                layer = []
                while len(layer) < nums:
                    node = stack.pop(0)
                    layer.append(node.val)

                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                nums = len(stack)
                res.insert(0, layer)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.levelOrderBottom(root))
