"""
Date: 2018/8/19
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        if numRows >= 1:
            res.append([1])
        if numRows >= 2:
            res.append([1, 1])

        for i in range(2, numRows):
            tmp = [1] * (i + 1)
            for j in range(1, len(tmp)-1):
                tmp[j] = res[-1][j-1] + res[-1][j]
            res.append(tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generate(6))