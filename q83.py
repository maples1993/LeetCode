"""
Date: 2018/8/18
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        p = head
        while p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(1)
    root.next.next = ListNode(1)
    root.next.next.next = ListNode(1)
    root.next.next.next.next = ListNode(1)

    s = Solution()
    p = s.deleteDuplicates(root)
    while p:
        print(p.val, end=' ')
        p = p.next