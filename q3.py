"""
Date: 2018/9/8
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        head = 0
        tail = 1
        char_dict = {s[head]: 1}

        max_len = 1
        cur_len = 1
        while tail < len(s):
            if s[tail] not in char_dict or char_dict[s[tail]] == 0:
                char_dict[s[tail]] = 1
                cur_len += 1
                tail += 1
            else:
                while s[head] != s[tail]:
                    char_dict[s[head]] = 0
                    head += 1
                    cur_len -= 1
                char_dict[s[head]] = 0
                head += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
        return max_len


print(Solution().lengthOfLongestSubstring('abcabcbb"'))
