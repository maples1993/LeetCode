"""
Date: 2018/9/5
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minimum = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if not self.minimum or x <= self.minimum[-1]:
            self.minimum.append(x)
        else:
            self.minimum.append(self.minimum[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop(-1)
        self.minimum.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minimum:
            return self.minimum[-1]
        else:
            return None
