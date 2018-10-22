class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        next = self.GetNext(needle)
        i = 0
        j = 0
        sLen = len(haystack)
        pLen = len(needle)
        while i < sLen and j < pLen:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == pLen:
            return i - j
        else:
            return -1

    def GetNext(self, p):
        pLen = len(p)
        next = [0 for i in range(pLen)]
        next[0] = -1
        k = -1
        j = 0
        while j < pLen - 1:
            if k == -1 or p[j] == p[k]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next