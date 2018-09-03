"""
Date: 2018/8/16
可以通过定义一个虚节点dummy，然后返回dummy.next解决没有头节点的问题
（否则需要单独的条件判断）
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1
        if not l1 and not l2:
            return None

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        elif l2:
            p.next = l2

        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(1)
    l2.next = ListNode(1)
    l2.next.next = ListNode(4)

    s = Solution()
    head = s.mergeTwoLists(l1, l2)
    while head:
        print(head.val, end=' ')
        head = head.next




