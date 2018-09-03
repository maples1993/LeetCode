"""
Date: 2018/8/15
解法1：水平扫描
解法2：竖直扫描
解法3：LCP(strs[0:k],strs[k+1:])，二分strs
解法4：二分第一个字符串
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''

        i = 0
        while True:
            try:
                common_c = strs[0][i]
                for s in strs:
                    if s[i] != common_c:
                        return prefix
                prefix += common_c
                i += 1
            except IndexError:
                return prefix


if __name__ == '__main__':
    strs = ['flower', 'flowerflow', 'flowerflight']

    s = Solution()
    print(s.longestCommonPrefix(strs))