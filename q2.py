"""
Date: 2018/9/6
各种小边界情况的判断
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2

        p1 = l1
        p2 = l2
        carry = 0
        tail = None
        while p1 and p2:
            add = p1.val + p2.val + carry
            if add >= 10:
                carry = 1
                p1.val = add % 10
            else:
                carry = 0
                p1.val = add
            if not p1.next:
                tail = p1
            p1 = p1.next
            p2 = p2.next

        if tail and p2:
            tail.next = p2
            p1 = p2

        while carry and p1:
            if p1.val == 9:
                p1.val = 0
            else:
                p1.val += 1
                carry = 0
            if not p1.next:
                tail = p1
            p1 = p1.next

        if carry:
            tail.next = ListNode(1)

        return l1
