# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        now = head
        list_len = 0
        while now is not None:
            list_len += 1
            now = now.next
        if list_len <= 1:
            return head
        k = k % list_len
        now, tail = head, head
        while k > 0:
            tail = tail.next
            k -= 1
        while tail.next is not None:
            tail = tail.next
            now = now.next
        tmp = now.next
        now.next = None
        tail.next = head
        return tmp


a = ListNode(5)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
e.next = d
d.next = c
c.next = b
b.next = a

s = Solution()
head = s.rotateRight(a, 3)
while head is not None:
    print head.val
    head = head.next