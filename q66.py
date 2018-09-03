"""
Date: 2018/8/17
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        bits = 1
        while carry == 0 and bits == 1 or \
                carry == 1 and bits <= len(digits):
            if digits[-bits] + 1 == 10:
                carry = 1
                digits[-bits] = 0
            else:
                digits[-bits] += 1
                carry = 0
            bits += 1
        if carry == 1:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    digits = [1, 2, 3]

    s = Solution()
    print(s.plusOne(digits))