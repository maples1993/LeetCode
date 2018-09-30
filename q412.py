"""
Date: 2018/9/26
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = [str(i) for i in range(1, n+1)]

        p3 = p5 = 1
        while True:
            index = min(p3 * 3, p5 * 5)
            if index > n:
                break
            if index == p3 * 3 == p5 * 5:
                ret[index - 1] = 'FizzBuzz'
                p3 += 1
                p5 += 1
            elif index == p3 * 3:
                ret[index - 1] = 'Fizz'
                p3 += 1
            elif index == p5 * 5:
                ret[index - 1] = 'Buzz'
                p5 += 1
        return ret

print(Solution().fizzBuzz(15))