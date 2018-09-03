"""
Date: 2018/8/21
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            res = [x + y for x, y in zip([0]+res, res+[0])]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(4))