class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        dp = [0 for _ in range(sLen)]
        maxLen = 0
        for i in range(1, sLen):
            cur = s[i]
            if cur == ")":
                pre = s[i-1]
                if pre == "(":
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                else:
                    preIdx = i - dp[i-1] - 1
                    if preIdx >= 0:
                        preMatch = s[preIdx]
                        if preMatch == "(":
                            dp[i] = dp[i-1] + 2 + (dp[preIdx-1] if preIdx-1 >= 0 else 0)
                maxLen = dp[i] if dp[i] > maxLen else maxLen
        return maxLen