"""
Date: 2018/9/8
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        new_head = ListNode('#')
        p = new_head
        while head:
            if head.val != val:
                p.next = head
                head = head.next
                p = p.next
                p.next = None
            else:
                head = head.next
        return new_head.next
