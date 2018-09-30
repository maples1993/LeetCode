"""
Date: 2018/9/14
"""


class Solution:
    def wordPattern(self, pattern, str_):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_ = str_.split()
        lsp = len(set(pattern))
        lss = len(set(str_))

        return len(pattern) == len(str_) \
               and lsp == lss \
               and lsp == len(set(zip(pattern, str_)))