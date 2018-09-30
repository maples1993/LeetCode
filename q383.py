"""
Date: 2018/9/20
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = {}
        for s in magazine:
            if s in mag_dict:
                mag_dict[s] += 1
            else:
                mag_dict[s] = 1

        ran_dict = {}
        for s in ransomNote:
            if s in ran_dict:
                ran_dict[s] += 1
            else:
                ran_dict[s] = 1

        for key in ran_dict:
            if key not in mag_dict or mag_dict[key] < ran_dict[key]:
                return False
        return True
