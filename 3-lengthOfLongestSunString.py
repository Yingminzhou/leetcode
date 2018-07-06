class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        for i in range(0, len(s)):
            nowLen = self.getLongestSubstring(s, i)
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
        if start == len(s):
            return 0
        nowDict[s[start]] = 1
        idx = start + 1
        while(idx < len(s)):
            if s[idx] not in nowDict:
                nowDict[s[idx]] = 1
                idx +=1
            else:
                break
        return len(nowDict)

if __name__ == '__main__':
    s = Solution()
    testStr = "c"
    testRes = s.lengthOfLongestSubstring(testStr)
    print testRes
