"""
Date: 2018/10/22
"""


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ret = []
        stack = [root]
        while stack:
            width = len(stack)
            layer = []
            while width:
                node = stack.pop(0)
                layer.append(node.val)
                for c in node.children:
                    stack.append(c)
                width -= 1
            ret.append(layer)
        return ret