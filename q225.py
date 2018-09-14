"""
Date: 2018/9/9
增加一个缓存队列，减小每次push的时间复杂度
"""


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = []
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.cache.append(x)
        for _ in range(len(self.cache) - 1):
            self.cache.append(self.cache.pop(0))

        if len(self.cache)**2 > len(self.queue):
            while len(self.queue) > 0:
                self.cache.append(self.queue.pop(0))

            self.cache, self.queue = self.queue, self.cache


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.cache:
            return self.cache.pop(0)
        else:
            return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.cache:
            return self.cache[0]
        else:
            return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.cache and not self.queue:
            return True
        else:
            return False

s = MyStack()
s.push(1)
s.push(2)