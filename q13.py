"""
Date: 2018/8/15
只要注意当小数在大数左边时，代表要减去这个数就可以了
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        integer = 0

        i = 0
        while i < len(s):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                integer = integer + roman[s[i+1]] - roman[s[i]]
                i += 1
            else:
                integer += roman[s[i]]
            i += 1
        return integer


if __name__ == '__main__':
    s = 'MCMXCIV'

    solu = Solution()
    print(solu.romanToInt(s))