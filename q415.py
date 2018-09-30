"""
Date: 2018/9/26
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num1 = list(num1)
        num2 = list(num2)

        carry = 0
        bits = 1
        while bits <= len(num2):
            tmp = int(num1[-bits]) + int(num2[-bits]) + carry
            if tmp >= 10:
                carry = 1
            else:
                carry = 0
            num1[-bits] = tmp % 10
            bits += 1

        while bits <= len(num1):
            tmp = int(num1[-bits]) + carry
            if tmp == 10:
                carry = 1
            else:
                carry = 0
            num1[-bits] = tmp % 10
            bits += 1

        if carry:
            num1.insert(0, 1)

        return ''.join(list(map(str, num1)))