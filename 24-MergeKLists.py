# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dumpyNode = ListNode(0)
        retList = dumpyNode
        currentK = self.getCurrentK(lists)
        while len(currentK) > 1:
            minIdx = 0
            minVal = currentK[minIdx].val
            for i in range(1, len(currentK)):
                nowVal = currentK[i].val
                if minVal > nowVal:
                    minVal = nowVal
                    minIdx = i
            retList.next = currentK[minIdx]
            retList = retList.next
            #print minIdx
            currentK[minIdx] = currentK[minIdx].next
            currentK = self.getCurrentK(currentK)
        if len(currentK) == 1:
            retList.next = currentK[0]
        return dumpyNode.next


    def getCurrentK(self, lists):
        retList = list()
        for i in range(len(lists)):
            if lists[i] is not None:
                retList.append(lists[i])
        return retList


a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f

g = ListNode(2)
h = ListNode(6)
g.next = h

lists = list()
#lists = [h, f.next, f]
lists = [a,d , g]

s = Solution()
dumpy = s.mergeKLists(lists)

while dumpy is not None:
    print dumpy.val
    dumpy = dumpy.next