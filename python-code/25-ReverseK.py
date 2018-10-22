# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        pre = h
        cur = head

        while cur != None:
            t = cur
            count = 1
            while count < k and t != None:
                t = t.next
                count += 1
            if count == k and t != None:
                for _ in range(k - 1):
                    lat = cur.next
                    cur.next = lat.next
                    lat.next = pre.next
                    pre.next = lat

                pre = cur
                cur = pre.next
            else:
                break

        return h.next
