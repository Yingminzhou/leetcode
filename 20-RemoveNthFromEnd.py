# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len = self.getLen(head)
        idx = len - n
        print len, idx
        if idx < 0:
            return head
        if idx == 0:
            return head.next
        ret = ListNode(0)
        ret.next = head
        while idx > 0:
            ret = ret.next
            idx -= 1
        ret.next = ret.next.next
        return head



    def getLen(self, head):
        len = 0
        tmp = ListNode(0)
        tmp.next = head
        while tmp.next is not None:
            len += 1
            tmp = tmp.next
        return len

s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
n = 5
res = s.removeNthFromEnd(a,n)
while res is not None:
    print res.val
    res = res.next