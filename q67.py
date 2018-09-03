"""
Date: 2018/8/18
每一位的加法其实就是carry+cur_sum，不需要那么多条件判断
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(map(int, a))[::-1]
        b = list(map(int, b))[::-1]
        res = ''

        carry = 0
        i = 0
        while i < len(a) and i < len(b):
            if a[i] & b[i] == 1:
                if carry == 1:
                    res += '1'
                else:
                    res += '0'
                    carry = 1
            elif a[i] ^ b[i] == 1:
                if carry == 1:
                    res += '0'
                else:
                    res += '1'
            else:
                if carry == 1:
                    res += '1'
                    carry = 0
                else:
                    res += '0'
            i += 1
        while i < len(b):
            if b[i] & carry == 1:
                res += '0'
            elif b[i] ^ carry == 1:
                res += '1'
                carry = 0
            else:
                res += '0'
            i += 1
        while i < len(a):
            if a[i] & carry == 1:
                res += '0'
            elif a[i] ^ carry == 1:
                res += '1'
                carry = 0
            else:
                res += '0'
            i += 1
        if carry == 1:
            res += '1'

        return res[::-1]

    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(map(int, a))
        b = list(map(int, b))
        res = []

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += a[i]
                i -= 1
            if j >= 0:
                sum += b[j]
                j -= 1
            res.append(sum % 2)
            carry = sum // 2
        if carry == 1:
            res.append(1)
        res = res[::-1]
        return ''.join([str(x) for x in res])


if __name__ == '__main__':
    a = '11'
    b = '1'

    s = Solution()
    print(s.addBinary2(a, b))
