"""
Date: 2018/9/9
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: boo
        """
        slow = fast = head

        # 找到中间节点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 翻转后半部分
        prev = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = prev
            prev = cur

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True