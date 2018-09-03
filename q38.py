"""
Date: 2018/8/17
题干不明，不用纠结
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))