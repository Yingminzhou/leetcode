class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        idx = 0
        while(idx<len(s)):
            idx, nowLen = self.getLongestSubstring(s, idx)
            if nowLen > maxLen:
                maxLen = nowLen
        return maxLen

    def getLongestSubstring(self, s, start):
        """
        :type s: str
        :type start: int
        :rtype: int
        """
        nowDict = dict()
        if start >= len(s):
            return 0
        nowDict[s[start]] = start
        idx = start + 1
        retIdx = len(s)
        while(idx < len(s)):
            if s[idx] not in nowDict:
                nowDict[s[idx]] = idx
                idx +=1
            else:
                retIdx = nowDict[s[idx]] + 1
                break
        return retIdx, len(nowDict)

if __name__ == '__main__':
    s = Solution()
    testStr = "abcdefadaf"
    testRes = s.lengthOfLongestSubstring(testStr)
    print testRes
