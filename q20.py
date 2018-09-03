"""
Date: 2018/8/16
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_par = []
        for c in s:
            if c in ['(', '{', '[']:
                left_par.append(c)

            if c == ')' and len(left_par) > 0 and left_par[-1] == '(':
                left_par.pop(-1)
            elif c == '}' and len(left_par) > 0 and left_par[-1] == '{':
                left_par.pop(-1)
            elif c == ']' and len(left_par) > 0 and left_par[-1] == '[':
                left_par.pop(-1)
            elif c in [')', '}', ']']:
                return False

        return len(left_par) == 0


if __name__ == '__main__':
    s = '{[]}'

    solu = Solution()
    print(solu.isValid(s))