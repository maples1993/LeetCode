"""
Date: 2018/9/26
"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                    6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                    12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        num &= 0xFFFFFFFF
        mask = 0x0000000F
        res = ''
        while num:
            key = num & mask
            res = hex_dict[key] + res
            num >>= 4
        if not res:
            res = '0'
        return res
