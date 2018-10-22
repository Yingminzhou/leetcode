# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(x):
    while x is not None:
        print x.val
        x = x.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dumpy = ListNode(0)
        head = dumpy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                dumpy.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dumpy.next = ListNode(l2.val)
                l2 = l2.next
            dumpy = dumpy.next
        if l1 is None:
            dumpy.next = l2
        else:
            dumpy.next = l1
        return head.next

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l4 = ListNode(4)
l1.next = l2
l2.next = l4


h1 = ListNode(1)
h3 = ListNode(3)
h4 = ListNode(4)
h1.next = h3
#h3.next = h4

printListNode(l1)
printListNode(h1)

print 'res'
printListNode(s.mergeTwoLists(l1, h1))