"""
Date: 2018/10/28
对于每个点，找到所有和它距离相等的点，然后选两个
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0] - q[0]
                s = p[1] - q[1]
                cmap[f * f + s * s] = 1 + cmap.get(f * f + s * s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] - 1)
        return res