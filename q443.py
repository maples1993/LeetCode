"""
Date: 2018/10/27
list多个元素直接替代，比insert快
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        while i < len(chars):
            count = 1
            l = r = i
            while r < len(chars) -1 and chars[r] == chars[r+1]:
                count += 1
                r += 1
            if count != 1:
                chars[l+1:r+1] = list(str(count))
                i = l + len(str(count))
            i += 1
        return len(chars)
