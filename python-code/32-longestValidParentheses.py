class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        parent = list()
        maxLen = 0
        curLen = 0
        for i in range(len(s)):
            cur = s[i]
            if cur == "(":
                parent.append(cur)
            else:
                if len(parent) == 0:
                    if maxLen < curLen:
                        maxLen = curLen
                    curLen = 0
                else:
                    parant = parent[:-1]
                    curLen += 1
        if maxLen < curLen:
            maxLen = curLen
        return maxLen * 2

