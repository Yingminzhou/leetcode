class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1 or len(s) == 0:
            return len(s)
        maxLen = 0
        idx = 0
        eIdx = 1
        flagList = s[idx]
        flagDict = {s[idx]: idx}
        while(idx<len(s) and eIdx < len(s)):
            if s[eIdx] not in flagList:
                flagList = s[idx : eIdx+1]
                flagDict[s[eIdx]] = eIdx
            else:
                nowLen = len(flagList)
                nowLen = eIdx - idx
                if nowLen > maxLen:
                    maxLen = nowLen
                idx = flagDict[s[eIdx]] + 1
                flagDict[s[eIdx]] = eIdx
                flagList = s[idx: eIdx+1]
            #print idx, eIdx, flagList
            eIdx += 1
        #print idx, eIdx
        nowLen = eIdx - idx
        if nowLen > maxLen:
            maxLen = nowLen
        return maxLen


if __name__ == '__main__':
    s = Solution()
    testStr = "ac"
    testRes = s.lengthOfLongestSubstring(testStr)
    print testRes
