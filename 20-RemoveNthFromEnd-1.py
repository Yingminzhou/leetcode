# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dumpy = ListNode(0)
        dumpy.next = head
        first = dumpy
        second = dumpy
        while n >= 0:
            first = first.next
            n -= 1
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dumpy.next