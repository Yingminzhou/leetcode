# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumpy = ListNode(0)
        dumpy.next = head
        nowTmp = dumpy
        while head is not None and head.next is not None:
            tmp = head.next
            tmpNext = tmp.next
            tmp.next = head
            head.next = tmpNext
            nowTmp.next = tmp
            nowTmp = head
            head = head.next
        return dumpy.next


a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

s = Solution()
dumpy = s.swapPairs(a)

while dumpy is not None:
    print dumpy.val
    dumpy = dumpy.next