"""
Date: 2018/9/6
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n &= 0xFFFFFFFF
        print(bin(n))
        res = 0 & 0xFFFFFFFF
        count = 0
        while count < 32:
            count += 1
            res <<= 1
            if n & 1 == 1:
                res += 1
            n >>= 1
        return res

print(Solution().reverseBits(43261596))