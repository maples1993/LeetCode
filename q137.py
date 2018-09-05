"""
Date: 2018/9/5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        p1 = head
        p2 = head.next
        while p2 != p1:
            if not p1 or not p2:
                return False
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
        return True