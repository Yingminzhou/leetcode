class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
    	nextDict = self.getNext(needle)
    	sLen = len(haystack)
    	pLen = len(needle)
    	i = 0
    	j = 0
    	while i < sLen:
            endIdx = i + pLen
            while j < pLen and i < sLen and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j < pLen and endIdx < sLen:
    	        endVal = haystack[endIdx]
                if endVal in nextDict:
                    #moving nextDict[endVal]
                    i = endIdx - pLen + nextDict[endVal]
        	else:
                    i = endIdx + 1
            	j = 0
            else:
                break
    	if j == pLen:
            return i - j
    	else:
            return -1

    def getNext(self, p):
    	nextDict = dict()
    	pLen = len(p)
    	for i in range(pLen):
        	nextDict[p[i]] = pLen - i
    	return nextDict


sl = Solution()
s = "mississippi"
p = "a"
print sl.strStr(s, p)
