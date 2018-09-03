"""
Date: 2018/8/17
要注意末尾有空格的特殊情况
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for x in s[::-1]:
            if x != ' ':
                count += 1
            elif x == ' ' and count > 0:
                break

        return count


if __name__ == '__main__':
    s = 'Hello World   '

    solu = Solution()
    print(solu.lengthOfLastWord(s))