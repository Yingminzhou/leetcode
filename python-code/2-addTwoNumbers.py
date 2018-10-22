# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """       
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1, l2 = self.sortNodeList(l1, l2)
        flag = 0
        retNode = l2
        pre = l2
        while l1 is not None or l2 is not None:
            if l1 is not None:
                nowSum = l1.val + l2.val + flag
            else:
                nowSum = l2.val + flag
            flag = nowSum / 10
            nowVal = nowSum % 10
            l2.val = nowVal
            if l1 is not None:
                l1 = l1.next
            pre = l2
            l2 = l2.next
        if flag > 0:
        	newNode = ListNode(flag)
        	pre.next = newNode
        return retNode



    # sort the two ListNodes
    def sortNodeList(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rType: ListNode, ListNode
        """
        now1 = l1
        now2 = l2
        while now1 is not None and now2 is not None:
            now1 = now1.next
            now2 = now2.next
        if now1 is None:
            return l1, l2
        else:
            return l2, l1
