"""
Date: 2018/10/22
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        if len(s) <= 0:
            return ret

        p_chars = {}
        p_length = len(p)
        for c in p:
            if c not in p_chars:
                p_chars[c] = 0
            p_chars[c] += 1

        start, end = 0, 0
        for end in range(len(s)):
            if s[end] not in p_chars:
                # print 'skipping ', s[end], ' at ', end
                while start < end:
                    p_chars[s[start]] += 1
                    start += 1
                start += 1
                continue

            # print 'try adding ', s[end], ' at ', end
            while p_chars[s[end]] == 0:
                p_chars[s[start]] += 1
                start += 1
                # print 'shifting start'
                # print start, p_chars
            p_chars[s[end]] -= 1
            if end - start + 1 == p_length:
                ret.append(start)

        return ret

