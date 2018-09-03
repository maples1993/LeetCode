"""
Date: 2018/8/21
"""


class Solution:
    def is_valid(self, c):
        return ord('a') <= ord(c) <= ord('z') \
               or ord('0') <= ord(c) <= ord('9')

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True

        s = s.lower()
        head = 0
        tail = len(s) - 1
        while head <= tail:
            if not self.is_valid(s[head]):
                head += 1
                continue
            if not self.is_valid(s[tail]):
                tail -= 1
                continue
            if s[head] == s[tail]:
                pass
            else:
                return False
            head += 1
            tail -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    sss = "a"
    sss2 = "A man, a plan, a canal: Panama"
    sss3 = "race a car"
    print(s.isPalindrome('oP'))