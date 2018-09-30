"""
Date: 2018/9/26
"""


class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def dfs(x, y, l):
            if l == 1:
                node = Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                tLeft = dfs(x, y, l // 2)
                tRight = dfs(x, y + l // 2, l // 2)
                bLeft = dfs(x + l // 2, y, l // 2)
                bRight = dfs(x + l // 2, y + l // 2, l // 2)
                value = tLeft.val or tRight.val or bLeft.val or bRight.val
                if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                    node = Node(value, True, None, None, None, None)
                else:
                    node = Node(value, False, tLeft, tRight, bLeft, bRight)
            return node

        return grid and dfs(0, 0, len(grid)) or None

x = Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
pass