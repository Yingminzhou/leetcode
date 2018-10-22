class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = self.removeConMark(p)
        if len(s) == 0:
            if len(p) == 0:
                return True
            elif p[0] == '*':
                return self.isMatch(s, p[1:])
            else:
                return False
        if len(p) == 0:
            return False
        if p[-1] == '?':
            return self.isMatch(s[:-1], p[:-1])
        elif p[-1] == '*':
            return self.isMatch(s, p[:-1]) or self.isMatch(s[:-1], p)
        else:
            return s[-1] == p[-1] and self.isMatch(s[:-1], p[:-1])


    def removeConMark(self, p):
        ans = ""
        for i in range(0, len(p)):
            if i >= 1 and p[i] == p[i-1] == "*":
                continue
            else:
                ans += p[i]
        return ans


sl = Solution()
s = "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
p = "***bba**a*bbba**aab**b"
print sl.isMatch(s, p)
print sl.removeConMark(p)


