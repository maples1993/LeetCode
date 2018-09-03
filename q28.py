"""
Date:2018/8/16
解法1：暴力循环，时间复杂度O(m*n)
解法2：KMP算法，主串指针不回溯，时间复杂度O(m+n)
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        if len(haystack) >= len(needle):
            try:
                return haystack.index(needle)
            except ValueError:
                return -1
        else:
            return -1

    # 暴力法
    def index(self, S, T):
        i = 0
        j = 0
        while i < len(S) and j < len(T):
            if S[i] == T[j]:
                i += 1
                j += 1
            else:
                i -= j - 1
                j = 0
        if j == len(T):
            return i - j
        else:
            return -1

    def get_next(self, T):
        i = 0
        j = -1
        next_val = [-1] * len(T)
        while i < len(T)-1:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # next_val[i] = j
                if i < len(T) and T[i] != T[j]:
                    next_val[i] = j
                else:
                    next_val[i] = next_val[j]
            else:
                j = next_val[j]
        return next_val

    def kmp(self, S, T):
        i = 0
        j = 0
        next = self.get_next(T)
        while i < len(S) and j < len(T):
            if j == -1 or S[i] == T[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(T):
            return i - j
        else:
            return -1


if __name__ == '__main__':
    haystack = 'acabaabaabcacaabc'
    needle = 'abaabcac'

    s = Solution()
    # print(s.get_next('aaaab'))
    print(s.kmp(haystack, needle))